from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

from calendar_events.serializers import CalendarEventSerializer
from calendar_events.models import CalendarEvent


class CalendarEventViewSet(ModelViewSet):
    queryset = CalendarEvent.objects.all()
    serializer_class = CalendarEventSerializer
#    def list(self, request):
#        queryset = CalendarEvent.objects.all()
#        serializer_class = CalendarEventSerializer(queryset,many=True)
#        return Response(serializer_class.data)