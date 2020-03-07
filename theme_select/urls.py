from theme_select.views import SelectThemeView
from django.conf.urls import url

urlpatterns = [
    url(r"^select_theme/$", SelectThemeView.as_view())
]
