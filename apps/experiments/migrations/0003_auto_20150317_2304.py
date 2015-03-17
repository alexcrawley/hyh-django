# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('experiments', '0002_auto_20150317_0035'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testgroup',
            name='target_percentage',
        ),
        migrations.AddField(
            model_name='experiment',
            name='active_status',
            field=models.CharField(default='Inactive', max_length=128, choices=[(b'Active', b'Active'), (b'Inactive', b'Inactive'), (b'Fallback', b'Fallback')]),
            preserve_default=False,
        ),
    ]
