import time

from rest_framework import serializers


def now() -> int:
    return int(time.time())


class ScheduleSerializer(serializers.Serializer):
    timestamp = serializers.IntegerField(default=now)
