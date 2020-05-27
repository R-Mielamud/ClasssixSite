from django.conf.urls import url
from diary_pdf.views import DiaryPdfView

urlpatterns = [
    url(r"^diary_pdf/$", DiaryPdfView.as_view())
]
