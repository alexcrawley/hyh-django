import collections

from django.db import models
from django.db.models import Sum

from apps.experiments import constants


class Experiment(models.Model):
    EXPERIMENT_TYPES = (
        (constants.EVENTS_ALGORITHM_EXPERIMENT, 'Compare events algorithms.'),
        )

    experiment_type = models.CharField(
        choices=EXPERIMENT_TYPES, max_length=128)

    name = models.CharField(primary_key=True, max_length=128)
    description = models.TextField(default="", blank=True, null=True)

    population_percentage = models.IntegerField()

    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)

    @property
    def num_users_in_experiment(self):
        return self.test_groups.aggregate(Sum('num_users'))['num_users__sum']

    def get_next_test_group(self):
        # #FIXME - ORDERED DICTSDICTS

        # # Which test group is furthest below it's target percentage.
        # total_users = self.num_users_in_experiment

        # test_groups_dict = {}
        # for test_group in self.test_groups.all():
        #     target = test_group.target_percentage
        #     actual = total_users / test_group.num_users

        #     diff = target - actual

        #     if diff > 0:
        #         test_groups_dict[test_group.pk] = diff

        # # Get the furthest away.
        # ordered = collections.OrderedDict(sorted(test_groups_dict.items()))

        # return self.test_groups.get(pk=ordered[0])
        return self.test_groups.all()[0]


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
        experiment = Experiment.objects.get(
            experiment_type=experiment_type
            )

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

    target_percentage = models.IntegerField()

    objects = TestGroupManager()
