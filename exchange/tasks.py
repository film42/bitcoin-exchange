from __future__ import absolute_import
from celery import shared_task
from bitcoin_exchange.celery import schedule_task
from datetime import timedelta
import requests
import json
from StringIO import StringIO
from models import Order, FilledStatusTypes

@shared_task
def synchronize_trades():
    trades_url = "http://darkpool.herokuapp.com/trades?limit=30"
    response = requests.get(trades_url)
    list_of_trades = json.load(StringIO(response.content))

    for trade in list_of_trades:
        order_guids = [trade["buyOrderId"], trade["sellOrderId"]]
        potential_orders = Order.objects.filter(guid=order_guids)

        for order in potential_orders:
            order.status = FilledStatusTypes.COMPLETE
            order.save()

            print order


# Schedule Tasks
schedule_task(
    'synchronize-trades-every-30-seconds', {
        'task': 'exchange.tasks.synchronize_trades',
        'schedule': timedelta(seconds=30),
    }
)
