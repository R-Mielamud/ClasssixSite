from errors.views import ErrorView
from django.conf.urls import url

urlpatterns = [
    url(r"^error/(?P<status>.{0,3})/(?P<phrase>.*)$", ErrorView.as_view())
]
