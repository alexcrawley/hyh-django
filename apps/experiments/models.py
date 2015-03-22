import random
from operator import xor

from django.core.exceptions import ValidationError

from apps.common import models
from apps.experiments import constants


class ExperimentManager(models.Manager):
    def get_for_user(self, user, experiment_type):
        """
            Determine if this user will take part in the active experiment.
        """
        try:
            experiment = Experiment.objects.get(
                active_status=constants.ACTIVE,
                experiment_type=experiment_type
                )
        except Experiment.DoesNotExist:
            experiment = None
        else:
            percentage = experiment.population_percentage
            random_number = random.randint(1, 100)

            if not random_number <= percentage:
                experiment = None
        finally:
            if experiment is None:
                return Experiment.objects.get_fallback(
                    user, experiment_type)
            else:
                return experiment

    def get_fallback(self, user, experiment_type):
        return Experiment.objects.get(
            active_status=constants.FALLBACK,
            experiment_type=experiment_type
            )

    def events(self):
        return Experiment.objects.filter(
            experiment_type=constants.EVENTS_ALGORITHM_EXPERIMENT
            )


class Experiment(models.ValidateModel):
    EXPERIMENT_TYPES = (
        (constants.EVENTS_ALGORITHM_EXPERIMENT, 'Compare events algorithms.'),
        )

    ACTIVE_STATUS = (
        (constants.ACTIVE, 'Active'),
        (constants.INACTIVE, 'Inactive'),
        (constants.FALLBACK, 'Fallback'),
        )

    experiment_type = models.CharField(
        choices=EXPERIMENT_TYPES, max_length=128)

    active_status = models.CharField(
        choices=ACTIVE_STATUS, max_length=128)

    name = models.CharField(max_length=128)
    description = models.TextField(default="", blank=True, null=True)

    population_percentage = models.IntegerField()

    objects = ExperimentManager()

    def __unicode__(self):
        return self.experiment_type + ' - ' + self.name

    def clean(self):
        # Check only
        this_experiment_active = self.active_status == constants.ACTIVE
        other_experiment_active = Experiment.objects.filter(
            experiment_type=self.experiment_type,
            active_status=constants.ACTIVE
            ).exclude(pk=self.pk).exists()

        if this_experiment_active and other_experiment_active:
            raise ValidationError(
                {'active_status': constants.EXPERIMENT_ALREADY_ACTIVE})

        # Check there is only one fallback experiment for this type.
        this_experiment_fallback = self.active_status == constants.FALLBACK
        other_experiment_fallback = Experiment.objects.filter(
            experiment_type=self.experiment_type,
            active_status=constants.FALLBACK
            ).exclude(pk=self.pk).exists()

        # Check only one experiment is fallback.
        if not (this_experiment_fallback or other_experiment_fallback):
            raise ValidationError(
                {'active_status': constants.EXPERIMENT_FALLBACK_REQUIRED})

        if not xor(this_experiment_fallback, other_experiment_fallback):
            raise ValidationError(
                {'active_status': constants.EXPERIMENT_FALLBACK_ALREADY_EXISTS}
                )

        # If this is fallback, require 100% population.
        if this_experiment_fallback and not self.population_percentage == 100:
            error_message = constants.EXPERIMENT_FALLBACK_100_PERCENT
            raise ValidationError(
                {'population_percentage': error_message})

    def get_next_test_group(self):
        return self.test_groups.order_by('-num_users')[0]


class TestGroupManager(models.Manager):
    def get_for_experiment(self, user, experiment_type):
        try:
            test_group = user.test_groups.get(
                experiment__experiment_type=experiment_type
                )
        except TestGroup.DoesNotExist:
            # Need to assign the user to a test group for this experiment.
            return self.assign_user_to_test_group(user, experiment_type)
        else:
            return test_group

    def assign_user_to_test_group(self, user, experiment_type):
        experiment = Experiment.objects.get_for_user(user, experiment_type)

        test_group = experiment.get_next_test_group()

        test_group.users.add(user)

        TestGroup.objects.filter(
            pk=test_group.pk).update(num_users=models.F('num_users') + 1)

        return test_group


class TestGroup(models.Model):
    ALGORITHM_CHOICES = (
        (constants.DEFAULT_EVENTS_ALGORITHM, 'Default'),
        (constants.RANDOM_EVENTS_ALGORITHM, 'Pseudo-Random events'),
    )

    experiment = models.ForeignKey(
        'experiments.Experiment', related_name='test_groups')
    algorithm = models.CharField(choices=ALGORITHM_CHOICES, max_length=256)
    users = models.ManyToManyField('users.User', related_name='test_groups')
    num_users = models.IntegerField(default=0)  # Denormalised for speed.

    objects = TestGroupManager()
