from django.contrib import admin
from diary.models import Subject, Rating, RatingSet, Month

admin.site.register(Subject)
admin.site.register(Rating)
admin.site.register(RatingSet)
admin.site.register(Month)
