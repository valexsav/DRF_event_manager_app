from rest_framework.serializers import ModelSerializer
from user.serializers import UserSerializer
from .models import Event

class EventSerializer(ModelSerializer):
    organizer = UserSerializer()

    class Meta:
        model = Event
        fields = (
            'pk',
            'title',
            'description',
            'date',
            'time',
            'total_tickets',
            'available_tickets',
            'location',
            'category',
            'organizer'
        )
