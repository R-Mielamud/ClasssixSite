from django.db.models import *
from main.models import User

class Article(Model):
    author = ForeignKey(User, related_name="articles", on_delete=CASCADE)
    header = CharField(default="", max_length=100)
    text = TextField(default="", max_length=1000)
    image = FileField(null=True, blank=True)
    video = FileField(null=True, blank=True)
