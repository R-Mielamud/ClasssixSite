from rest_framework.viewsets import ModelViewSet
from api.serializers import ArticleSerializer, UserSerializer, SubjectSerializer, RatingSerializer, RatingSetSerializer, MonthSerializer
from news.models import Article
from main.models import User
from diary.models import Month, Subject, Rating, RatingSet
from . import constants
import hashlib

class ApiKeyRequiredModelViewSet(ModelViewSet):
    def get_queryset_with_checking(self, fulfiled, rejected):
        apikey = self.request.query_params.get("apikey")

        if (not apikey) or (apikey != constants.APIKEY):
            return rejected
        else:
            return fulfiled

class GetLastTenArticlesViewSet(ApiKeyRequiredModelViewSet):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        return super().get_queryset_with_checking(Article.objects.order_by("-id")[:10], [])

class IsUserExistsViewSet(ApiKeyRequiredModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        username = self.request.query_params.get("username")
        password = self.request.query_params.get("password")

        if password:
            hashsed_password = hashlib.md5(hashlib.md5(password.encode()).hexdigest().encode()).hexdigest()

            return super().get_queryset_with_checking(
                User.objects.filter(username=username, password=hashsed_password),
                []
            )
        else:
            return []

class IsUserExistsMd5ViewSet(ApiKeyRequiredModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        username = self.request.query_params.get("username")
        password = self.request.query_params.get("password")

        if password:
            return super().get_queryset_with_checking(
                User.objects.filter(username=username, password=password),
                []
            )
        else:
            return []

class GetMonthsViewSet(ApiKeyRequiredModelViewSet):
    serializer_class = MonthSerializer
    
    def get_queryset(self):
        return super().get_queryset_with_checking(
            Month.objects.order_by("number_in_year"),
            []
        )

class GetSubjectsViewSet(ApiKeyRequiredModelViewSet):
    serializer_class = SubjectSerializer

    def get_queryset(self):
        return super().get_queryset_with_checking(
            Subject.objects.order_by("index"),
            []
        )

class GetUserRatingsViewSet(ApiKeyRequiredModelViewSet):
    serializer_class = RatingSetSerializer

    def get_queryset(self):
        username = self.request.query_params.get("username")
        user = User.objects.filter(username=username)

        if user:
            user = user.first()
            return super().get_queryset_with_checking(user.ratings.all(), [])
        else:
            return []
