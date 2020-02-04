from django.conf.urls import url
from editratings.views import EditratingsView

urlpatterns = [
    url(r"^editratings/$", EditratingsView.as_view())
]
