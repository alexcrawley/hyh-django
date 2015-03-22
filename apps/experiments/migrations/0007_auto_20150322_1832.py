# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps.common.fields


class Migration(migrations.Migration):

    dependencies = [
        ('experiments', '0006_auto_20150322_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiment',
            name='population_percentage',
            field=apps.common.fields.IntegerRangeField(),
            preserve_default=True,
        ),
    ]
