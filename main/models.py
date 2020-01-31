from django.db.models import *

class User(Model):
    ratings = ManyToManyField("diary.RatingSet", related_name="students", blank=True)
    class_rating = DecimalField(null=True, blank=True, max_digits=5, decimal_places=3)
    is_teacher = BooleanField(default=False)
    username = CharField(default="", max_length=100)
    password = CharField(default="", max_length=100)
