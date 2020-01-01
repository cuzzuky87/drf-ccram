from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cal_events import views

router = DefaultRouter()
router.register('calendar_events', views.CalendarEventViewSet)

app_name='cal_events'

urlpatterns = [
    path('', include(router.urls))
]