from apps.experiments.models import Experiment
from apps.experiments import constants


class ExperimentsTestMixin(object):
    def create_experiment(self, **kwargs):
        experiment_dict = dict(
            experiment_type=constants.EVENTS_ALGORITHM_EXPERIMENT,
            active_status=constants.FALLBACK,
            name='Fallback',
            population_percentage=100
        )

        experiment_dict.update(kwargs)

        Experiment.objects.create(**experiment_dict)

    def create_fallback_experiment(self, **kwargs):
        return self.create_experiment(**kwargs)

    def create_active_experiment(self, **kwargs):
        experiment_dict = dict(
            active_status=constants.ACTIVE,
            name='Active',
            )

        experiment_dict.update(kwargs)

        return self.create_experiment(**experiment_dict)
