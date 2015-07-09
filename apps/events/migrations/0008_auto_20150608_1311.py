# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_auto_20150607_2119'),
    ]

    operations = [
        migrations.AddField(
            model_name='tevocategory',
            name='name',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tevocategory',
            name='parent',
            field=models.ForeignKey(to='events.TevoCategory', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tevocategory',
            name='slug',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
    ]
