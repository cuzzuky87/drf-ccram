from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APIClient
from django.utils import timezone

from calendar_events.models import CalendarEvent
from calendar_events.serializers import CalendarEventSerializer

CALENDAR_EVENT_URL = reverse('calendar_events:calendarevent-list')

class PublicCalendarEventApiTest(TestCase):
    """Test the publicly available calendar event api"""

    def setUp(self):
        self.client = APIClient()
    
    def test_login_required(self):
        """Test that login is required for retrieving calendar events"""
        res = self.client.get(CALENDAR_EVENT_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

class PrivateCalendarEventApiTest(TestCase):
    """Test the authorized users calendar event API"""

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            "test@gmail.com",
            "testPassw0rd"
        )
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_retieve_calendar_events(self):
        """Test retrieving calenadar event"""
        CalendarEvent.objects.create(
            user=self.user,
            title="Meeting",
            start_at=timezone.now(),
            end_at=timezone.now() + timezone.timedelta(hours=2)
        )
        CalendarEvent.objects.create(
            user=self.user,
            title="coding",
            start_at=timezone.now(),
            end_at=timezone.now() + timezone.timedelta(hours=3)
        )

        res = self.client.get(CALENDAR_EVENT_URL)

        events = CalendarEvent.objects.all().order_by('-name')
        serializer = CalendarEventSerializer(CalendarEvent, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)