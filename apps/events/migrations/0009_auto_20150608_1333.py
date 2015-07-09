# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_auto_20150608_1311'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tevocategory',
            name='tevo_url',
        ),
        migrations.RemoveField(
            model_name='tevoclient',
            name='tevo_url',
        ),
        migrations.RemoveField(
            model_name='tevoconfiguration',
            name='tevo_url',
        ),
        migrations.RemoveField(
            model_name='tevoevent',
            name='tevo_url',
        ),
        migrations.RemoveField(
            model_name='tevoperformer',
            name='tevo_url',
        ),
        migrations.RemoveField(
            model_name='tevovenue',
            name='tevo_url',
        ),
    ]
