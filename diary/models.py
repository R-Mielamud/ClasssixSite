from django.db.models import *
from . import constants

class Subject(Model):
    name = CharField(default="", max_length=100)
    index = IntegerField(default=1)

    def __str__(self):
        return "{}".format(self.name)

class Rating(Model):
    value = PositiveIntegerField(null=True, blank=True)
    color = CharField(null=True, blank=True, max_length=100)
    status = CharField(choices=constants.RATING_TYPES, null=True, blank=True, max_length=100)

    def _set_color(self):
        self.color = constants.STATUS_TYPE_TO_COLOR[self.status]

    def save(self, *args, **kwargs):
        if self.pk is None:
            super().save(*args, **kwargs)

        self._set_color()
        return super().save(*args, **kwargs)

class RatingSet(Model):
    rating1 = ForeignKey(Rating, related_name="sets1", on_delete=CASCADE, blank=True, null=True)
    rating2 = ForeignKey(Rating, related_name="sets2", on_delete=CASCADE, blank=True, null=True)
    rating3 = ForeignKey(Rating, related_name="sets3", on_delete=CASCADE, blank=True, null=True)
    rating4 = ForeignKey(Rating, related_name="sets4", on_delete=CASCADE, blank=True, null=True)
    subject = ForeignKey(Subject, related_name="sets", on_delete=CASCADE)
    day = IntegerField(default=1)
    month = IntegerField(default=1)

class Month(Model):
    days = IntegerField(default=30)
    name = CharField(default="", max_length=30)
    semester = IntegerField(default=1)
    number_in_semester = IntegerField(default=1)
    number_in_year = IntegerField(default=1)
