# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('experiments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testgroup',
            name='num_users',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
