import datetime
from typing import Tuple

import holidays
import pytz
from django.conf import settings
from django.utils.functional import classproperty


class Schedule:
    @classproperty
    def period(self) -> int:
        return settings.SCHEDULE_PERIOD

    @classproperty
    def start_date(self) -> datetime.date:
        return settings.SCHEDULE_START_DATE

    @classproperty
    def shift_a(self) -> Tuple[datetime.time, datetime.time]:
        return settings.SCHEDULE_SHIFT_A_START, settings.SCHEDULE_SHIFT_A_END

    @classproperty
    def shift_b(self) -> Tuple[datetime.time, datetime.time]:
        return settings.SCHEDULE_SHIFT_B_START, settings.SCHEDULE_SHIFT_B_END

    @classmethod
    def utc_to_sst(cls, timestamp) -> datetime.datetime:
        utc_dt = datetime.datetime.utcfromtimestamp(timestamp)
        local_tz = pytz.timezone(settings.TIME_ZONE)
        return utc_dt.replace(tzinfo=pytz.utc).astimezone(local_tz)

    @classmethod
    def is_holiday(cls, date: datetime.date) -> bool:
        return date in holidays.Canada(prov=settings.SCHEDULE_PROVINCE)

    @classmethod
    def is_working(cls, sst: datetime.datetime) -> bool:
        date = sst.date()
        time = sst.time()

        delta_days = (date - cls.start_date).days
        delta_periods = int((delta_days - (delta_days % cls.period)) / cls.period)

        # even periods are on
        # odd periods are off
        is_period_on = delta_periods % 2 == 0

        if is_period_on and not cls.is_holiday(date):
            on_periods = int(delta_periods / 2)

            # even on periods are shift a
            # odd on periods are shift b
            shift = cls.shift_a if on_periods % 2 == 0 else cls.shift_b
            return shift[0] <= time <= shift[1]

        return False
