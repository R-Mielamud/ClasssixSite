from rest_framework.viewsets import ModelViewSet
from api.serializers import ArticleSerializer, UserSerializer
from news.models import Article
from main.models import User
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

class ExistsUserViewSet(ApiKeyRequiredModelViewSet):
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
