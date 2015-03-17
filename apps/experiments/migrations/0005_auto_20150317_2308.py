# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('experiments', '0004_create_default_experiment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='experiment',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='experiment',
            name='start_date',
        ),
    ]
