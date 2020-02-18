from rest_framework import routers
from django.conf.urls import url, include
from api.views import GetLastTenArticlesViewSet, ExistsUserViewSet

router = routers.DefaultRouter()
router.register(r"get_last_ten_articles", GetLastTenArticlesViewSet, basename="article")
router.register(r"is_user_exists", ExistsUserViewSet, basename="user")

urlpatterns = [
    url(r"^", include(router.urls))
]
