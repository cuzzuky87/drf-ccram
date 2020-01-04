from django.urls import path, include
from rest_framework.routers import DefaultRouter

from calendar_events import views

router = DefaultRouter()
router.register('calendar_events', views.CalendarEventViewSet)

app_name='calendar_events'

urlpatterns = [
    path('', include(router.urls))
]