from django.conf.urls import url
from editratings.views import EditRatingsView

urlpatterns = [
    url(r"^editratings/$", EditRatingsView.as_view())
]
