# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Experiment',
            fields=[
                ('experiment_type', models.CharField(max_length=128, choices=[(b'Events Algorithm', b'Compare events algorithms.')])),
                ('name', models.CharField(max_length=128, serialize=False, primary_key=True)),
                ('description', models.TextField(default=b'', null=True, blank=True)),
                ('population_percentage', models.IntegerField()),
                ('start_date', models.DateTimeField(null=True, blank=True)),
                ('end_date', models.DateTimeField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TestGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('algorithm', models.CharField(max_length=256, choices=[(b'Default', b'Default'), (b'Random', b'Pseudo-Random events')])),
                ('num_users', models.IntegerField()),
                ('target_percentage', models.IntegerField()),
                ('experiment', models.ForeignKey(related_name='test_groups', to='experiments.Experiment')),
                ('users', models.ManyToManyField(related_name='test_groups', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
