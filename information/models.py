from django.db.models import *
from diary.models import Subject

class TeacherData(Model):
    full_name = CharField(max_length=100, default="")
    subject = ForeignKey(Subject, on_delete=CASCADE, related_name="teacher_data_sets")

    def __str__(self):
        return "{} | {}".format(self.full_name, self.subject)

    class Meta:
        verbose_name_plural = "Teacher data sets"

class ScheduleSubject(Model):
    day_number = IntegerField(default=1)
    day_index = IntegerField(default=1)
    subject = CharField(default="", max_length=200)
    cabinet = CharField(default="31", max_length=10)

    def __str__(self):
        return "{} {} {} {}".format(self.day_number, self.day_index, self.subject, self.cabinet)
