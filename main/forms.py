from django.forms import *
from main.models import User
import hashlib

class RegistrationForm(Form):
    username = CharField(required=True, widget=TextInput(attrs={"autocomplete": "off"}))
    password = CharField(widget=PasswordInput, required=True)

    def _get_user(self):
        data = self.cleaned_data
        password_level_1 = hashlib.md5(data["password"].encode()).hexdigest()
        password_level_2 = hashlib.md5(password_level_1.encode()).hexdigest()
        user_queryset = User.objects.filter(username=data["username"], password=password_level_2)
        user = user_queryset.first()
        return user

    @property
    def can_register_user(self):
        user = self._get_user()
        return True if user else False
    
    def get_username(self):
        return self._get_user().username
