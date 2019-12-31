from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APIClient

from cal_events.models import CalendarEvent
from cal_events.serializer import CalendarEventSerializer

CALENDAR_EVENT_URL = reverse('cal_events:calendar-events-list')

class PublicCalendarEventApiTest(TestCase):
    """Test the publicly available calendar event api"""

    def setUp(self):
        self.client = APIClient()
    
    def test_login_required(self):
        """Test that login is required for retrieving calendar events"""
        res = self.client.get(CALENDAR_EVENT_URL)

        self.assertEqual(res.status, status.HTTP_401_UNAUTHORIZED)

class PrivateCalendarEventApiTest(TestCase):
    """Test the authorized users calendar event API"""

    def setUp(self):
        self.user = get_user_model(
            "test@gmail.com",
            "testPassw0rd"
        )
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_retieve_calendar_events(self):
        """Test retrieving calenadar event"""
        CalendarEvent.objects.create(user=self.user, title="Meeting")
        CalendarEvent.objects.create(user=self.user, title="coding")

        res = self.client.get(CALENDAR_EVENT_URL)

        events = CalendarEvent.objects.all().order_by('-name')
        serializer = CalendarEventSerializer(CalendarEvent, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)