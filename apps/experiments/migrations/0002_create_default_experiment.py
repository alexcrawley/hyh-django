# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from apps.experiments import constants


class Migration(migrations.Migration):

    dependencies = [
        ('experiments', '0001_initial'),
    ]

    def create_default_experiment(apps, schema_editor):
        Experiment = apps.get_model("experiments", "Experiment")
        TestGroup = apps.get_model("experiments", "TestGroup")

        experiment = Experiment.objects.create(
            experiment_type=constants.EVENTS_ALGORITHM_EXPERIMENT,
            active_status=constants.FALLBACK,
            name='Fallback',
            population_percentage=100,
            )

        test_group = TestGroup.objects.create(
            experiment=experiment,
            algorithm=constants.DEFAULT_EVENTS_ALGORITHM,
            )

    operations = [
        migrations.RunPython(create_default_experiment),
    ]
