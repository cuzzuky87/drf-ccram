import uuid
from django.db import models

from accounts.models import CustomUser


class CalendarEvent(models.Model):
    """Calendar model"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    title = models.CharField(max_length=100)
    description = models.TextField()
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    start_at = models.DateTimeField()
    end_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
