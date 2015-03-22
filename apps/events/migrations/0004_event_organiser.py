# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_organiser'),
        ('events', '0003_auto_20150308_1751'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='organiser',
            field=models.ForeignKey(default=0, to='users.Organiser'),
            preserve_default=False,
        ),
    ]
