from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings
from celery.task import periodic_task
from celery.schedules import crontab
from diary import constants
import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ClasssixSite.settings")
app = Celery("ClasssixSite")

app.config_from_object("django.conf:settings")
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.task(bind=True)
def debug_task(self):
    print("Request: {0!r}".format(self.request))

@app.task
def work_with_POST(Post, request):
    from diary.models import Rating, RatingSet, Subject
    from main.models import User
    print("adfhg")

    year = str(datetime.datetime.now()).split("-")[0]
    dates = request["showing_dates"] or [str(day) + ".09." + year for day in range(1, 11, 1)]

    for student in User.objects.filter(is_teacher=False):
        rating_sets = []

        for date in dates:
            ratings = list()
            
            for i in range(1, 5, 1):
                rating = Post.get("set-rating-mini-form-rating-input-{}-{}-for-date-{}".format(i, student.pk, date))
                stauts = Post.get("set-rating-mini-form-status-input-{}-{}-for-date-{}".format(i, student.pk, date))

                if rating:
                    ratings.append(Rating(value=rating, status=stauts))

            for r in ratings:
                r.save()

            month = int(date.split(".")[1])
            month_formatted = month - 8 if month > 8 else month + 4

            if len(ratings) > 0:
                rating_sets.append(RatingSet(
                    rating1=ratings[0] if len(ratings) >= 1 else None,
                    rating2=ratings[1] if len(ratings) >= 2 else None,
                    rating3=ratings[2] if len(ratings) >= 3 else None,
                    rating4=ratings[3] if len(ratings) >= 4 else None,
                    month=month_formatted,
                    day=date.split(".")[0],
                    subject=Subject.objects.get(name=request["subject"]) or Subject.objects.all().first()
                ))

        for rs in rating_sets:
            rs.save()
            student.ratings.add(rs)
        
        student.save()

@periodic_task(
    run_every=(crontab(day_of_month="*/1")),
    name="set_days_in_February",
    ignore_result=True
)
def set_days_in_February():
    from diary.models import Month

    February = Month.objects.get(name=constants.SECOND_MONTH_IN_YEAR_NANE)

    if int(str(datetime.datetime.now()).split("-")[0]) % 4 == 0:
        February.days = 29
        February.save()
    else:
        February.days = 28
        February.save()
