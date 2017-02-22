from __future__ import absolute_import
from celery import Celery

# celery -A friend.celery worker -l info

CELERY_BROKER_URL = 'redis://localhost:6379/2'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/2'

celery = Celery(__file__, broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)

@celery.task
def hit(a, b):
	return a+b



def count(a, b):
	while a < b:
		yield a+b
		a += 1

@celery.task
def spread_another_cpu(a, b):
	b *= 1000000
	return sum([ i for i in count(a, b) ]) 
