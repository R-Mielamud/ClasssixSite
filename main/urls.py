from django.conf.urls import url
from main.views import RegistrationAndMainView

urlpatterns = [
    url(r"^$", RegistrationAndMainView.as_view())
]
