from django.test import TestCase
from django.core.exceptions import ValidationError

from apps.experiments.models import Experiment
from apps.experiments import constants
from apps.experiments.tests.mixins import ExperimentsTestMixin
from apps.users.models import User


class TestExperimentModelValidation(TestCase, ExperimentsTestMixin):
    def test_only_one_fallback_experiment_permitted(self):
        # DEFAULT EVENTS EXPERIMENT ALREADY CREATED IN MIGRATIONS.
        try:
            self.create_fallback_experiment()
        except ValidationError as e:
            error_dict = e.error_dict
        else:
            error_dict = {}

        self.assertEqual(
            str(error_dict.get('active_status', None)[0][0]),
            constants.EXPERIMENT_FALLBACK_ALREADY_EXISTS)

    def test_fallback_experiment_required(self):
        # DEFAULT EVENTS EXPERIMENT ALREADY CREATED IN MIGRATIONS.
        fallback_experiment = Experiment.objects.get(
            experiment_type=constants.EVENTS_ALGORITHM_EXPERIMENT,
            active_status=constants.FALLBACK,
            )

        # Try and make it inactive, should get an error.
        fallback_experiment.active_status = constants.INACTIVE
        try:
            fallback_experiment.save()
        except ValidationError as e:
            error_dict = e.error_dict
        else:
            error_dict = {}

        self.assertEqual(
            str(error_dict.get('active_status', None)[0][0]),
            constants.EXPERIMENT_FALLBACK_REQUIRED)

    def test_fallback_100_percent_required(self):
        # DEFAULT EVENTS EXPERIMENT ALREADY CREATED IN MIGRATIONS.
        fallback_experiment = Experiment.objects.get(
            experiment_type=constants.EVENTS_ALGORITHM_EXPERIMENT,
            active_status=constants.FALLBACK,
            )

        # Try and make it less than 100 percent.
        fallback_experiment.population_percentage = 50
        try:
            fallback_experiment.save()
        except ValidationError as e:
            error_dict = e.error_dict
        else:
            error_dict = {}

        self.assertEqual(
            str(error_dict.get('population_percentage', None)[0][0]),
            constants.EXPERIMENT_FALLBACK_100_PERCENT)

    def test_only_one_active_experiment_permitted(self):
        # Create one active experiment
        self.create_active_experiment(**dict(name='Active1'))

        # Try and create another.
        try:
            self.create_active_experiment(**dict(name='Active2'))
        except ValidationError as e:
            error_dict = e.error_dict
        else:
            error_dict = {}

        self.assertEqual(
            str(error_dict.get('active_status', None)[0][0]),
            constants.EXPERIMENT_ALREADY_ACTIVE)


class TestExperimentManager(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='regular_user1@example.com',
            email='regular_user1@example.com',
            password='testing'
            )

        self.fallback_experiment = Experiment.objects.get(
            experiment_type=constants.EVENTS_ALGORITHM_EXPERIMENT,
            active_status=constants.FALLBACK,
            )

    def test_get_fallback(self):
        self.assertEqual(
            Experiment.objects.get_fallback(
                experiment_type=constants.EVENTS_ALGORITHM_EXPERIMENT
                ),
            self.fallback_experiment
            )


class TestExperimentMigrations(TestCase):
    def test_fallback_experiment_and_test_group_created(self):
        fallback_experiment = Experiment.objects.get(
            experiment_type=constants.EVENTS_ALGORITHM_EXPERIMENT,
            active_status=constants.FALLBACK,
            population_percentage=100
            )

        self.assertTrue(bool(fallback_experiment.pk))

        # Fallback experiment has a test group.
        self.assertEqual(fallback_experiment.test_groups.count(), 1)
