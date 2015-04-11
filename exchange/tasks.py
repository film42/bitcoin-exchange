from __future__ import absolute_import
from celery import shared_task
from celery.utils.log import get_task_logger
from bitcoin_exchange.celery import schedule_task
from datetime import timedelta
import requests
import json
from StringIO import StringIO
from exchange.models import Order, FilledStatusTypes

logger = get_task_logger(__name__)

@shared_task
def synchronize_trades():
    trades_url = "http://darkpool.herokuapp.com/trades?limit=30"
    response = requests.get(trades_url)
    list_of_trades = json.load(StringIO(response.content))

    for trade in list_of_trades:
        order_guids = [str(trade["buyOrderId"]), str(trade["sellOrderId"])]
        potential_orders = Order.objects.filter(guid__in=order_guids)

        for order in potential_orders:
            logger.info("Updating trade: %s" % str(order.guid))
            order.status = FilledStatusTypes.COMPLETE
            order.save()


# Schedule Tasks
schedule_task(
    'synchronize-trades-every-5-seconds', {
        'task': 'exchange.tasks.synchronize_trades',
        'schedule': timedelta(seconds=5),
    }
)
