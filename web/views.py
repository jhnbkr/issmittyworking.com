import datetime
import time

from django.views.generic import TemplateView

from smitty.utils import Schedule


class HomeView(TemplateView):
    template_name = "web/home.html"

    @property
    def timestamp(self) -> int:
        if "timestamp" in self.request.GET:
            try:
                return int(self.request.GET["timestamp"])
            except ValueError:
                pass
        return int(time.time())

    @property
    def sst(self) -> datetime.datetime:
        return Schedule.utc_to_sst(self.timestamp)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_working"] = Schedule.is_working(self.sst)
        return context
