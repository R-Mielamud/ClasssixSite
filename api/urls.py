from rest_framework import routers
from django.conf.urls import url, include

from api.views import (
    GetLastTenArticlesViewSet,
    IsUserExistsViewSet,
    IsUserExistsMd5ViewSet,
    GetMonthsViewSet,
    GetSubjectsViewSet,
    GetUserRatingsViewSet
)

router = routers.DefaultRouter()
router.register(r"get_last_ten_articles", GetLastTenArticlesViewSet, basename="article")
router.register(r"is_user_exists", IsUserExistsViewSet, basename="user")
router.register(r"is_user_exists_md5", IsUserExistsMd5ViewSet, basename="user")
router.register(r"get_months", GetMonthsViewSet, basename="month")
router.register(r"get_subjects", GetSubjectsViewSet, basename="subject")
router.register(r"get_user_ratings", GetUserRatingsViewSet, basename="ratingset")

urlpatterns = [
    url(r"^", include(router.urls))
]
