from errors.views import ErrorView
from django.conf.urls import url

urlpatterns = [
    url(r"^error/(?P<status>.*)$", ErrorView.as_view())
]
