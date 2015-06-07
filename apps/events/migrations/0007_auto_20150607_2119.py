# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_auto_20150607_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tevoevent',
            name='category',
            field=models.ForeignKey(to='events.TevoCategory', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tevoevent',
            name='configuration',
            field=models.ForeignKey(to='events.TevoConfiguration', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tevoevent',
            name='performers',
            field=models.ManyToManyField(to='events.TevoPerformer', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tevoevent',
            name='venue',
            field=models.ForeignKey(to='events.TevoVenue', null=True),
            preserve_default=True,
        ),
    ]
