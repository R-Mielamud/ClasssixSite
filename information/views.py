from information.models import ScheduleSubject, TeacherData
from main.views import RegistrationFormView

class InformationView(RegistrationFormView):
    template_name = "information.html"
    success_url = "/information/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["monday_subjects"] = ScheduleSubject.objects.filter(day_number=1).order_by("day_index")
        context["tuesday_subjects"] = ScheduleSubject.objects.filter(day_number=2).order_by("day_index")
        context["wednesday_subjects"] = ScheduleSubject.objects.filter(day_number=3).order_by("day_index")
        context["thursday_subjects"] = ScheduleSubject.objects.filter(day_number=4).order_by("day_index")
        context["friday_subjects"] = ScheduleSubject.objects.filter(day_number=5).order_by("day_index")
        context["teacher_data_sets"] = TeacherData.objects.all()
        return context
