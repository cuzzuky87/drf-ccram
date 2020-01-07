from rest_framework import serializers

from calendar_events.models import CalendarEvent
from accounts.serializers import CustomUserSerializer

class CalendarEventSerializer(serializers.Serializer):
    """Serializer for Calendar Event object"""
    class Meta:
        model = CalendarEvent
        fields = (
            'id',
            'title',
            'description',
            'user',
            'start_at',
            'end_at',
            'created_at',
            'modified_at',
        )