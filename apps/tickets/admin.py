from django.contrib import admin

from apps.tickets.models import Ticket


class TicketAdmin(admin.ModelAdmin):
    list_display = [
        'event',
        'user',
        'quantity',
        'price',
        ]

    list_filter = [
        'event',
        ]

    search_fields = [
        'event__title',
        'user',
        ]


admin.site.register(Ticket, TicketAdmin)
