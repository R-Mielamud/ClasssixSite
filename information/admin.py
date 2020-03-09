from django.contrib import admin
from information.models import ScheduleSubject, TeacherData

def reg(*models):
    for model in models:
        admin.site.register(model)

reg(ScheduleSubject, TeacherData)
