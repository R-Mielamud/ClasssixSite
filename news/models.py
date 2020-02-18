from django.db.models import *
from main.models import User

class Article(Model):
    author = ForeignKey(User, related_name="articles", on_delete=CASCADE)
    date = DateField(auto_now_add=True)
    header = CharField(default="", max_length=100)
    text = TextField(default="", max_length=1000)
    image = FileField(null=True, blank=True)
    video = FileField(null=True, blank=True)

    def __str__(self):
        return "\"{}\" {} {}".format(self.header, self.author.real_full_name, self.date)
