from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings
from celery.task import periodic_task
from celery.decorators import task
from celery.schedules import crontab
from diary import constants
import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ClasssixSite.settings")
app = Celery("ClasssixSite")

app.config_from_object("django.conf:settings")
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@task(bind=True)
def debug_task(self):
    print("Request: {0!r}".format(self.request))

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
