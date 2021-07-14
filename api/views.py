from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from api.serializers import ScheduleSerializer
from smitty.utils import Schedule


class ScheduleView(GenericAPIView):
    serializer_class = ScheduleSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)

        date = serializer.validated_data["date"]
        time = serializer.validated_data["time"].replace(microsecond=0)

        return Response(
            {
                "date": date,
                "time": time,
                "is_holiday": Schedule.is_holiday(date),
                "is_working": Schedule.is_working(date, time),
            },
            status=status.HTTP_200_OK,
        )
