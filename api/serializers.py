from rest_framework.serializers import ModelSerializer
from main.models import User
from news.models import Article
from diary.models import Rating, RatingSet, Subject, Month

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password", "real_full_name"]

class ArticleSerializer(ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Article
        fields = ["author", "header", "text", "image", "video"]

class RatingSerializer(ModelSerializer):
    class Meta:
        model = Rating
        fields = ["value", "color"]

class SubjectSerializer(ModelSerializer):
    class Meta:
        model = Subject
        fields = ["index", "name"]

class MonthSerializer(ModelSerializer):
    class Meta:
        model = Month
        fields = ["name", "days", "number_in_semester", "number_in_year"]

class RatingSetSerializer(ModelSerializer):
    subject = SubjectSerializer()
    rating1 = RatingSerializer()
    rating2 = RatingSerializer()
    rating3 = RatingSerializer()
    rating4 = RatingSerializer()

    class Meta:
        model = RatingSet
        fields = ["month", "day", "subject", "rating1", "rating2", "rating3", "rating4"]
