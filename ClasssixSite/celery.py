from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings
from . import settings as proj_settings
from celery.task import periodic_task, task
from celery.schedules import crontab
from diary import constants
from django.core import mail
import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ClasssixSite.settings")
app = Celery("ClasssixSite")

app.config_from_object("django.conf:settings")
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.task(bind=True)
def debug_task(self):
    print("Request: {0!r}".format(self.request))

@task
def send_emails(data):
    from main.models import User

    emails = User.objects.filter(is_subscriber=True).values_list("email", flat=True)

    if not proj_settings.DEBUG:
        if data["is_string"]:
            mail.send_mail(
                data["subject"],
                data["message"],
                data["from"],
                emails,
                fail_silently=proj_settings.DEBUG
            )
        else:
            mail.send_mail(
                subject=data["subject"],
                message="",
                from_email=data["from"],
                html_message=data["message"],
                recipient_list=emails,
                fail_silently=proj_settings.DEBUG
            )

@task
def work_with_POST(inputs, showing_dates, subject, is_test):
    from diary.models import Rating, RatingSet, Subject
    from main.models import User

    def format_date_component(component):
        if component >= 10:
            return str(component)
        else:
            return "0{}".format(component)

    year = str(datetime.datetime.now()).split("-")[0]
    dates = showing_dates or [format_date_component(day) + ".09." + year for day in range(1, 31, 1)]

    for student in User.objects.filter(is_teacher=False, is_test=is_test):
        for date in dates:
            ratings = list()
            
            for i in range(1, 5, 1):
                rating = inputs.get("rating-input-{}-{}-date-{}".format(i, student.index, date))
                stauts = inputs.get("status-input-{}-{}-date-{}".format(i, student.index, date))

                if rating:
                    rating = Rating(value=rating, status=stauts)
                    rating.save()
                    ratings.append(rating)

            month = int(date.split(".")[1])
            month_formatted = month - 8 if month > 8 else month + 4

            if len(ratings) > 0:
                rating_set = RatingSet(
                    rating1=ratings[0] if len(ratings) >= 1 else None,
                    rating2=ratings[1] if len(ratings) >= 2 else None,
                    rating3=ratings[2] if len(ratings) >= 3 else None,
                    rating4=ratings[3] if len(ratings) >= 4 else None,
                    month=month_formatted,
                    day=date.split(".")[0],
                    subject=Subject.objects.get(name=subject) if subject else Subject.objects.all().first()
                )

                rating_set.save()
                student.ratings.add(rating_set)

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

@periodic_task(
    run_every=(crontab(minute="*/1")),
    name="calculate_middle_ratings",
    ignore_result=True
)
def calculate_middle_ratings():
    from main.models import User
    students = User.objects.filter(is_teacher=False)

    for student in students:
        rating_sets = student.ratings.all()
        rating_sets_dict = {}
        rating_sets_list = []

        for rating_set in rating_sets:
            if rating_sets_dict.get("{}-{}".format(rating_set.month, rating_set.day)):
                rating_sets_dict["{}-{}".format(rating_set.month, rating_set.day)].append(rating_set)
            else:
                rating_sets_dict["{}-{}".format(rating_set.month, rating_set.day)] = [rating_set]

        for date in rating_sets_dict:
            rating_set = rating_sets_dict[date][len(rating_sets_dict[date]) - 1]

            if ((rating_set.rating1.value != 0 if rating_set.rating1 else True)
                and (rating_set.rating2.value != 0 if rating_set.rating2 else True)
                and (rating_set.rating3.value != 0 if rating_set.rating3 else True)
                and (rating_set.rating4.value != 0 if rating_set.rating4 else True)):
                    rating_sets_list.append(rating_set)

        rating_sum = 0
        ratings_count = 0

        for rating_set in rating_sets_list:
            if rating_set.rating1:
                rating_sum += rating_set.rating1.value
                ratings_count += 1

            if rating_set.rating2:
                rating_sum += rating_set.rating2.value
                ratings_count += 1

            if rating_set.rating3:
                rating_sum += rating_set.rating3.value
                ratings_count += 1

            if rating_set.rating4:
                rating_sum += rating_set.rating4.value
                ratings_count += 1
        
        middle_rating = round(rating_sum / ratings_count, 2) if ratings_count != 0 else 12
        student.middle_rating = middle_rating
        student.save()
