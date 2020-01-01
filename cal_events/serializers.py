from rest_framework import serializers

from cal_events.models import CalendarEvent

class CalendarEventSerializer(serializers.Serializer):
    """Serializer for Calendar Event object"""

    class Meta:
        model = CalendarEvent
        field = ('title','description','start_at','end_at')