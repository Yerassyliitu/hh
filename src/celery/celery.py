# celery -A src.celery.tasks worker --loglevel=INFO --pool=solo
# celery -A src.celery.tasks flower
# flower will be available on http://localhost:5555/
# celery -A src.celery.tasks beat
from celery import Celery



celery = Celery('hh_tasks', broker='redis://localhost:6379')

