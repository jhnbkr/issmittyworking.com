import datetime

from django.views.generic import TemplateView

from smitty.utils import Schedule


class HomeView(TemplateView):
    template_name = "web/home.html"

    @property
    def date(self) -> datetime.date:
        if "date" in self.request.GET:
            try:
                return datetime.datetime.strptime(
                    self.request.GET["date"], "%Y-%m-%d"
                ).date()
            except ValueError:
                pass

        return Schedule.get_date_now()

    @property
    def time(self) -> datetime.time:
        if "time" in self.request.GET:
            try:
                return datetime.datetime.strptime(
                    self.request.GET["time"], "%H:%M:%S"
                ).time()
            except ValueError:
                pass

        return Schedule.get_time_now()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_working"] = Schedule.is_working(self.date, self.time)
        return context
