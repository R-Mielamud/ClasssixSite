from django.forms import *
from main.models import User
from diary import constants

class EditRatingsForm(Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        students = User.objects.filter(is_teacher=False)

        for student in students:
            for i in range(4):
                self.fields[student.username + "_status_" + str(i)] = ChoiceField(choices=constants.RATING_TYPES, required=False)
                self.fields[student.username + "_rating_" + str(i)] = IntegerField(max_value=12, min_value=1, required=False)

            self.fields[student.username + "_date"] = DateField(required=False)
