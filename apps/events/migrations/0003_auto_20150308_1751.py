# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20150301_2112'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='eventuserresponse',
            unique_together=set([]),
        ),
    ]
