from main.views import RegistrationFormView
from diary.models import Subject, Month
from main.models import User
from diary import constants
import datetime

class EditratingsView(RegistrationFormView):
    success_url = "/editratings/"
    template_name = "editratings.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        year = str(datetime.datetime.now()).split("-")[0]

        o_month = Month.objects.filter(name=self.request.session.get("month_name")).first()

        context["showing_dates"] = self.request.session.get("showing_dates") or [str(day) + ".09." + year for day in range(1, 11, 1)]
        context["max_date"] = o_month.days if o_month else 30
        context["month_name"] = o_month.name if o_month else context["months"][0].name
        context["subject_name"] = self.request.session["subject"]
        context["subjects"] = Subject.objects.all()
        context["students"] = User.objects.filter(is_teacher=False)
        context["months"] = Month.objects.all()
        context["rating_statuses"] = constants.RATING_TYPES

        return context

    def _format_date_component(self, component):
        if component >= 10:
            return component
        else:
            return "0{}".format(component)

    def post(self, request, *args, **kwargs):
        Post = request.POST

        if Post.get("config"):
            month = Post.get("month_name_input")
            o_month = Month.objects.get(name=month)

            year = str(datetime.datetime.now()).split("-")[0]

            month_num = o_month.number_in_year + 8 if o_month.number_in_year < 5 else o_month.number_in_year - 4

            formatted_month_num = self._format_date_component(month_num)

            request.session["showing_dates"] = [
                "{}.{}.{}".format(self._format_date_component(day), formatted_month_num, year)
                for day in range(1, o_month.days + 1, 1)
            ]

            request.session["month_name"] = month
            request.session["subject"] = Post.get("subject_name_input")

        return super().post(request, *args, **kwargs)
