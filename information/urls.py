from information.views import InformationView
from django.conf.urls import url

urlpatterns = [
    url(r"^information/$", InformationView.as_view())
]
