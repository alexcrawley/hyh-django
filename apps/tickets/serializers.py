from rest_framework import serializers

from apps.tickets.models import Ticket


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'event', 'quantity', 'user')
        model = Ticket


class CreateTicketSerializer(serializers.ModelSerializer):
    stripe_token = serializers.CharField(write_only=True)

    class Meta:
        model = Ticket
        fields = ('stripe_token', 'event', 'quantity', 'user',)

    def create(self, validated_data):
        return Ticket.objects.create_ticket(**validated_data)
