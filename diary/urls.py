from django.conf.urls import url
from diary.views import DiaryView

urlpatterns = [
    url(r"^diary/", DiaryView.as_view())
]
