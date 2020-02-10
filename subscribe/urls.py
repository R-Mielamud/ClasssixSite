from subscribe.views import SubscribeView, UnsubscribeView
from django.conf.urls import url

urlpatterns = [
    url(r"^subscribe/$", SubscribeView.as_view()),
    url(r"^unsubscribe/$", UnsubscribeView.as_view())
]
