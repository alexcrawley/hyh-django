# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import apps.experiments.model_services
import apps.common.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Experiment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('experiment_type', models.CharField(max_length=128, choices=[(b'Events Algorithm', b'Compare events algorithms.')])),
                ('active_status', models.CharField(max_length=128, choices=[(b'Active', b'Active'), (b'Inactive', b'Inactive'), (b'Fallback', b'Fallback')])),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField(default=b'', null=True, blank=True)),
                ('population_percentage', apps.common.fields.IntegerRangeField()),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, apps.experiments.model_services.ExperimentServices),
        ),
        migrations.CreateModel(
            name='TestGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('algorithm', models.CharField(max_length=256, choices=[(b'Default', b'Default'), (b'Random', b'Pseudo-Random events')])),
                ('num_users', models.IntegerField(default=0)),
                ('experiment', models.ForeignKey(related_name='test_groups', to='experiments.Experiment')),
                ('users', models.ManyToManyField(related_name='test_groups', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
