# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps.events.models.model_services


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_remove_event_organiser'),
    ]

    operations = [
        migrations.CreateModel(
            name='TevoCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tevo_id', models.IntegerField(unique=True)),
                ('tevo_url', models.URLField(unique=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, apps.events.models.model_services.BaseTevoModelService),
        ),
        migrations.CreateModel(
            name='TevoClient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tevo_id', models.IntegerField(unique=True)),
                ('tevo_url', models.URLField(unique=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, apps.events.models.model_services.BaseTevoModelService),
        ),
        migrations.CreateModel(
            name='TevoConfiguration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tevo_id', models.IntegerField(unique=True)),
                ('tevo_url', models.URLField(unique=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, apps.events.models.model_services.BaseTevoModelService),
        ),
        migrations.CreateModel(
            name='TevoEvent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tevo_id', models.IntegerField(unique=True)),
                ('tevo_url', models.URLField(unique=True)),
                ('name', models.CharField(max_length=1000)),
                ('occurs_at', models.DateTimeField()),
                ('state', models.CharField(max_length=1000)),
                ('stubhub_id', models.CharField(max_length=1000)),
                ('owned_by_office', models.BooleanField(default=False)),
                ('available_count', models.IntegerField()),
                ('products_count', models.IntegerField()),
                ('popularity_score', models.DecimalField(max_digits=20, decimal_places=6)),
                ('long_term_popularity_score', models.DecimalField(max_digits=20, decimal_places=6)),
                ('category', models.ForeignKey(to='events.TevoCategory')),
                ('configuration', models.ForeignKey(to='events.TevoConfiguration')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, apps.events.models.model_services.BaseTevoModelService),
        ),
        migrations.CreateModel(
            name='TevoPerformer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tevo_id', models.IntegerField(unique=True)),
                ('tevo_url', models.URLField(unique=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, apps.events.models.model_services.BaseTevoModelService),
        ),
        migrations.CreateModel(
            name='TevoVenue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tevo_id', models.IntegerField(unique=True)),
                ('tevo_url', models.URLField(unique=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, apps.events.models.model_services.BaseTevoModelService),
        ),
        migrations.AddField(
            model_name='tevoevent',
            name='performers',
            field=models.ManyToManyField(to='events.TevoPerformer'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tevoevent',
            name='venue',
            field=models.ForeignKey(to='events.TevoVenue'),
            preserve_default=True,
        ),
    ]
