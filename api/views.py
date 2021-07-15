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

        timestamp = serializer.validated_data["timestamp"]

        try:
            sst = Schedule.utc_to_sst(timestamp)
        except (ValueError, OverflowError):
            sst = Schedule.utc_to_sst(Schedule.timestamp_now())

        return Response(
            {
                "utc": timestamp,
                "sst": sst,
                "is_working": Schedule.is_working(sst),
            },
            status=status.HTTP_200_OK,
        )
