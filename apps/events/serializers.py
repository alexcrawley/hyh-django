from rest_framework import serializers

from apps.events.models import Event, EventUserResponse


class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'title', 'img',)


class EventUserResponseSerializer(serializers.ModelSerializer):
    event = EventSerializer()

    class Meta:
        model = EventUserResponse
        fields = ('id', 'user', 'event', 'response',)
