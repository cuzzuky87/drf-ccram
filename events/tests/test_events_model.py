from django.test import TestCase
from django.contrib.auth import get_user_model

from . import models

def test_user(email="test@gmail.com", password="TestP4ssw0rd"):
    """Create a test user"""
    return get_user_model().objects.create_user(email, password)

class EventModelTests(TestCase):
    def test_event_str(self):
        event = models.Event.objects.create(
            user=test_user(),
            title="test_events"
        )

        self.assertEqual(str(event), event.title)