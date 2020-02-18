from rest_framework.serializers import ModelSerializer
from main.models import User
from news.models import Article

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password"]

class ArticleSerializer(ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Article
        fields = ["author", "header", "text", "image", "video"]