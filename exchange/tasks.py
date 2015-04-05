from __future__ import absolute_import
from celery import shared_task
from bitcoin_exchange.celery import schedule_task
from datetime import timedelta


@shared_task
def add(x, y):
    return x + y


# Schedule Tasks
schedule_task(
    'add-every-30-seconds', {
        'task': 'exchange.tasks.add',
        'schedule': timedelta(seconds=30),
        'args': (16, 16)
    }
)
