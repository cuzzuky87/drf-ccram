from django.test import TestCase
from django.contrib.auth import get_user_model
from django.utils import timezone

from calendar_events.models import CalendarEvent

def sample_user(email="test@gmail.com", password="TestP4ssw0rd"):
    """Create a test user"""
    return get_user_model().objects.create_user(email, password)

class EventModelTests(TestCase):
    def test_event_str(self):
        event = CalendarEvent.objects.create(
            user=sample_user(),
            title="test_events",
            start_at = timezone.now(),
            end_at = timezone.now() + timezone.timedelta(days=1)
        )

        self.assertEqual(str(event), event.title)