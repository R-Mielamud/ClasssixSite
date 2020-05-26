from diary.models import Subject, Month
from main.models import User
from main.views import RegistrationFormView
from diary import constants

class DiaryView(RegistrationFormView):
    template_name = "diary.html"
    success_url = "/diary/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_user = None

        if not self.request.session.get("registered"):
            context["canRedirect"] = "y"
        else:
            username = self.request.session.get("registered")
            current_user = User.objects.get(username=username)

        if current_user.is_teacher:
            context["canRedirect"] = "y"

        subjects = Subject.objects.all()
        context["subjects"] = subjects.order_by("index")
        context["subjects_len"] = len(subjects)
        context["ratings"] = current_user.ratings.all()
        context["middle_rating"] = current_user.middle_rating
        context["first_semester_months"] = Month.objects.filter(semester=1).order_by("number_in_semester")
        context["second_semester_months"] = Month.objects.filter(semester=2).order_by("number_in_semester")
        context["status_to_color"] = constants.STATUS_TYPE_TO_COLOR
        return context
