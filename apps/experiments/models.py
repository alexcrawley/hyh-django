import random
from django.db import models

from apps.experiments import constants


class ExperimentManager(models.Manager):
    def get_for_user(self, user, experiment_type):
        """
            Determine if this user will take part in the active experiment.
        """
        try:
            experiment = Experiment.objects.get(
                active_status=constants.ACTIVE_STATUS,
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


class Experiment(models.Model):
    EXPERIMENT_TYPES = (
        (constants.EVENTS_ALGORITHM_EXPERIMENT, 'Compare events algorithms.'),
        )

    ACTIVE_STATUS = (
        (constants.ACTIVE_STATUS, 'Active'),
        (constants.INACTIVE_STATUS, 'Inactive'),
        (constants.FALLBACK, 'Fallback'),
        )

    experiment_type = models.CharField(
        choices=EXPERIMENT_TYPES, max_length=128)

    active_status = models.CharField(
        choices=ACTIVE_STATUS, max_length=128)

    name = models.CharField(primary_key=True, max_length=128)
    description = models.TextField(default="", blank=True, null=True)

    population_percentage = models.IntegerField()

    objects = ExperimentManager()

    def __unicode__(self):
        return self.experiment_type + ' - ' + self.name

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
