import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

app = Celery('myproject')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

from celery.schedules import crontab

app.conf.beat_schedule = {
    'run-test-task-every-5-seconds': {
        'task': 'core.tasks.test_celery',
        'schedule': 5.0,  # every 5 seconds
    },
}

app.conf.timezone = 'UTC'
