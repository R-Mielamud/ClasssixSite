from diary.models import Subject, Month
from main.views import RegistrationFormView
from . import constants
import datetime

class DiaryView(RegistrationFormView):
    template_name = "diary.html"
    success_url = "/diary/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if not self.request.session.get("registered"):
            context["canRedirect"] = "y"

        subjects = Subject.objects.all()
        context["subjects"] = subjects
        context["subjects_len"] = len(subjects)
        context["first_semester_months"] = Month.objects.filter(semester=1).order_by("number_in_semester")
        context["second_semester_months"] = Month.objects.filter(semester=2).order_by("number_in_semester")
        February = Month.objects.get(name=constants.SECOND_MONTH_IN_YEAR_NANE)

        if int(str(datetime.datetime.now()).split("-")[0]) % 4 == 0:
            February.days = 29
            February.save()
        else:
            February.days = 28
            February.save()

        return context
