from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from cal_events.serializers import CalendarEventSerializer
from cal_events.models import CalendarEvent


class CalendarEventViewSet(ModelViewSet):
    serializer_class = CalendarEventSerializer
    queryset = CalendarEvent.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)