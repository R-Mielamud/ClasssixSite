from django.db.models import *

class User(Model):
    ratings = ManyToManyField("diary.RatingSet", related_name="students", blank=True)
    real_full_name = CharField(default="", max_length=100)
    class_rating = DecimalField(null=True, blank=True, max_digits=5, decimal_places=3)
    is_teacher = BooleanField(default=False)
    username = CharField(default="", max_length=100)
    password = CharField(default="", max_length=100)
    email = EmailField(null=True, blank=True)
    is_subscriber = BooleanField(default=False)
    index = IntegerField(blank=True, null=True)

    def __str__(self):
        return "{}".format(self.real_full_name)
