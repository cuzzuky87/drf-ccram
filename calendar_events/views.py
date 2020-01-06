from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from calendar_events.serializers import CalendarEventSerializer
from calendar_events.models import CalendarEvent


class CalendarEventViewSet(ModelViewSet):
    serializer_class = CalendarEventSerializer
    queryset = CalendarEvent.objects.all()