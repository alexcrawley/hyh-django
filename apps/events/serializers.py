from rest_framework import serializers

from apps.events.models import Event, EventUserResponse
from apps.events import constants
from apps.users.models import User


class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'title', 'img',)


class EventUserResponseSerializer(serializers.ModelSerializer):
    event = EventSerializer()

    class Meta:
        model = EventUserResponse
        fields = ('id', 'user', 'event', 'response',)

    def create(self, validated_data):
        user = User.objects.get(pk=validated_data['user'])
        event = Event.objects.get(pk=validated_data['event']['pk'])
        response = validated_data['response']

        if response == constants.LIKE:
            event_response = user.like_event(event)
        elif response == constants.DISLIKE:
            event_response = user.dislike_event(event)

        return event_response
