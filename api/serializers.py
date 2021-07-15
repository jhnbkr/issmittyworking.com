from rest_framework import serializers

from smitty.utils import Schedule


class ScheduleSerializer(serializers.Serializer):
    timestamp = serializers.IntegerField(default=Schedule.timestamp_now)
