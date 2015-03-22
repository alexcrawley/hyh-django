# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from decimal import Decimal
from django.conf import settings
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20150308_1751'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('method', models.CharField(max_length=256, choices=[(b'Stripe', b'Stripe')])),
                ('amount_currency', djmoney.models.fields.CurrencyField(default=b'GBP', max_length=3, editable=False, choices=[(b'GBP', 'Pound Sterling')])),
                ('amount', djmoney.models.fields.MoneyField(decimal_places=2, default=Decimal('0.0'), currency_choices=[(b'GBP', 'Pound Sterling')], max_digits=18, verbose_name=b'Payment Amount', default_currency=b'GBP')),
                ('reference_num', models.CharField(max_length=256)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('price_currency', djmoney.models.fields.CurrencyField(default=b'GBP', max_length=3, editable=False, choices=[(b'GBP', 'Pound Sterling')])),
                ('price', djmoney.models.fields.MoneyField(decimal_places=2, default=Decimal('0.0'), currency_choices=[(b'GBP', 'Pound Sterling')], max_digits=18, verbose_name=b'Ticket Price', default_currency=b'GBP')),
                ('event', models.ForeignKey(related_name='tickets', to='events.Event')),
                ('user', models.ForeignKey(related_name='tickets', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='payment',
            name='ticket',
            field=models.OneToOneField(to='tickets.Ticket'),
            preserve_default=True,
        ),
    ]
