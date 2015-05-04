# coding: utf-8
#
import logging
from celery import shared_task
from celery.task import periodic_task
from celery.schedules import crontab

logger = logging.getLogger('django')


@periodic_task(run_every=crontab())
def test():
    print "HELLO"


@periodic_task(run_every=crontab(hour="*", minute="*", day_of_week="*"))
def test1():
    print "HELLO"


@shared_task
def add(x, y):
    x, y = 1, 2
    return x + y
