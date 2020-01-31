from django.forms import *
from main.models import User

class RegistrationForm(Form):
    username = CharField()
    password = CharField(widget=PasswordInput)

    def _get_user(self):
        data = self.cleaned_data
        user_queryset = User.objects.filter(username=data["username"], password=data["password"])
        user = user_queryset.first()
        return user

    @property
    def can_register_user(self):
        user = self._get_user()
        return True if user else False
    
    def get_username(self):
        return self._get_user().username
