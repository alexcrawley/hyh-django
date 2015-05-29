from rest_framework import serializers

from apps.tickets.models import Ticket


class TicketSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = ('id', 'event', 'quantity',)
        model = Ticket
        depth = 1


class CreateTicketSerializer(serializers.ModelSerializer):
    stripe_token = serializers.CharField(write_only=True)

    class Meta:
        model = Ticket
        fields = ('stripe_token', 'event', 'quantity', 'user',)

    def create(self, validated_data):
        return Ticket.objects.create_ticket(**validated_data)
