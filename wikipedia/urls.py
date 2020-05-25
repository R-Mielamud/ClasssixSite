from django.conf.urls import url
from wikipedia.views import WikipediaView

urlpatterns = [
    url(r"^wikipedia/$", WikipediaView.as_view())
]
