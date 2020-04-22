from django.conf.urls import url
from main.views import RegistrationAndMainView, StopSpamView

urlpatterns = [
    url(r"^$", RegistrationAndMainView.as_view()),
    url(r"^stop_spam/$", StopSpamView.as_view())
]
