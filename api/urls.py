from django.urls import path

from api.views import ScheduleView

urlpatterns = [
    path("schedule/", ScheduleView.as_view(), name="schedule"),
]
