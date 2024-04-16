# celery -A src.celery.tasks worker --loglevel=INFO --pool=solo
# celery -A src.celery.tasks flower
# flower will be available on http://localhost:5555/
# celery -A src.celery.tasks beat
from celery import Celery
from celery.schedules import crontab



celery = Celery('hh_tasks', broker='redis://localhost:6379')

celery.conf.beat_schedule = {
    'send-every-day': {
        'task': 'src.celery.tasks.regular_alert_daily',
        'schedule': crontab(hour=7, minute=30, day_of_week='1-6'),
    },
    'send-every-week': {
        'task': 'src.celery.tasks.regular_alert_weekly',
        'schedule': crontab(hour=16, minute=0, day_of_week='sun'),
    },
}