from .celery import celery


celery.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task': 'src.celery.tasks.test',
        'schedule': 5.0,

    },
}

@celery.task
def test():
    return "Hello"