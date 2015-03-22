# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('experiments', '0005_auto_20150317_2308'),
    ]

    operations = [
        migrations.AddField(
            model_name='experiment',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=1, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='experiment',
            name='name',
            field=models.CharField(max_length=128),
            preserve_default=True,
        ),
    ]
