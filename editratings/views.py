from main.views import RegistrationFormView
from diary.models import Subject, Month, RatingSet
from main.models import User
from diary import constants
from ClasssixSite.celery import work_with_POST
import datetime
from django.shortcuts import redirect

class EditratingsView(RegistrationFormView):
    success_url = "/editratings/"
    template_name = "editratings.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        year = str(datetime.datetime.now()).split("-")[0]

        o_month = Month.objects.filter(name=self.request.session.get("month_name")).first()

        registered = self.request.session.get("registered")

        user = User.objects.filter(username=registered).first()

        show_ratings_by = self.request.session.get("ratings_subject") or "Укр. мова"
        o_show_ratings_by = Subject.objects.get(name=show_ratings_by)

        context["showing_dates"] = self.request.session.get("showing_dates") or [str(self._format_date_component(day)) + ".09." + year for day in range(1, 31, 1)]
        context["max_date"] = o_month.days if o_month else 30
        context["subjects"] = Subject.objects.all().order_by("index")
        context["subject_name"] = self.request.session.get("subject") or context["subjects"][0].name
        context["students"] = User.objects.filter(is_teacher=False).order_by("index")
        context["students_len"] = len(context["students"])
        context["months"] = Month.objects.all().order_by("number_in_year")
        context["month_name"] = o_month.name if o_month else context["months"][0].name
        context["rating_statuses"] = [status[0] for status in constants.RATING_TYPES]
        context["first_semester_months"] = Month.objects.filter(semester=1).order_by("number_in_semester")
        context["second_semester_months"] = Month.objects.filter(semester=2).order_by("number_in_semester")
        context["canRedirect"] = "n" if registered and user.is_teacher else "y"
        context["ratings"] = RatingSet.objects.filter(subject=o_show_ratings_by)

        return context

    def _format_date_component(self, component):
        if component >= 10:
            return component
        else:
            return "0{}".format(component)
        
    def _work_with_POST(self, inputs, showing_dates, subject):
        work_with_POST.delay(inputs, showing_dates, subject)

    def post(self, request, *args, **kwargs):
        if not request.session.get("registered"):
            return redirect("/")
        else:
            user = User.objects.get(username=request.session.get("registered"))

            if not user.is_teacher:
                return redirect("/")

        if request.POST.get("config"):
            month = request.POST.get("month_name_input")
            o_month = Month.objects.get(name=month)

            year = str(datetime.datetime.now()).split("-")[0]

            month_num = o_month.number_in_year + 8 if o_month.number_in_year < 5 else o_month.number_in_year - 4

            formatted_month_num = self._format_date_component(month_num)

            request.session["showing_dates"] = [
                "{}.{}.{}".format(self._format_date_component(day), formatted_month_num, year)
                for day in range(1, o_month.days + 1, 1)
            ]

            request.session["month_name"] = month
            request.session["subject"] = request.POST.get("subject_name_input")
        elif request.POST.get("save_ratings"):
            inputs = {key: request.POST[key] for key in request.POST if key[7:12:1] == "input"}
            self._work_with_POST(inputs, request.session.get("showing_dates"), request.session.get("subject"))
        elif request.POST.get("show-subject"):
            request.session["ratings_subject"] = request.POST.get("showing-subject")
        
        return super().post(request, *args, **kwargs)
