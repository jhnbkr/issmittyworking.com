from rest_framework import serializers

from smitty.utils import Schedule


class ScheduleSerializer(serializers.Serializer):
    date = serializers.DateField(default=Schedule.get_date_now)
    time = serializers.TimeField(default=Schedule.get_time_now)
