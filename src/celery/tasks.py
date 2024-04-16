from .celery import celery


celery.conf.beat_schedule = {
    'send-every-day': {
        'task': 'src.celery.tasks.test',
        'schedule': 86400,
    },
    'send-every-week': {
        'task': 'src.celery.tasks.test',
        'schedule': 345600,
    },
}

@celery.task
def test():
    return "Hello"