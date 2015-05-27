from django.db import models
from django.conf import settings

from djmoney.models.fields import MoneyField

from apps.tickets import constants


class TicketManager(models.Manager):
    def create_ticket(self, **kwargs):
        # FIXME - Make charge from token
        kwargs.pop('stripe_token')

        return Ticket.objects.create(**kwargs)


class Ticket(models.Model):
    event = models.ForeignKey('events.Event', related_name='tickets')
    quantity = models.IntegerField()

    user = models.ForeignKey('users.User', related_name='tickets')

    price = MoneyField(
        "Ticket Price",
        default_currency=settings.DEFAULT_CURRENCY_CODE,
        currency_choices=settings.CURRENCY_CHOICES,
        max_digits=18, decimal_places=2,
        )

    objects = TicketManager()


class Payment(models.Model):
    PAYMENT_METHODS = (
        (constants.STRIPE, 'Stripe'),
        )

    ticket = models.OneToOneField('tickets.Ticket',)

    method = models.CharField(max_length=256, choices=PAYMENT_METHODS)

    amount = MoneyField(
        "Payment Amount",
        default_currency=settings.DEFAULT_CURRENCY_CODE,
        currency_choices=settings.CURRENCY_CHOICES,
        max_digits=18, decimal_places=2,
        )

    reference_num = models.CharField(max_length=256, null=True)
