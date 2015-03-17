from django.test import TestCase
from models import *
from decimal import *


class OrderCRUD(TestCase):

    def test_crud_order(self):
        order = Order.objects.create(amount=5, limit=5)
        self.assertEqual(order.amount, 5)
        self.assertEqual(order.from_currency, '')
        self.assertEqual(order.limit, 5)

        #update
        order.amount = 10
        order.from_currency = 'r'
        order.limit = 3
        order.save()

        #read
        self.assertEqual(order.amount, 10)
        self.assertEqual(order.from_currency, 'r')
        self.assertEqual(order.limit, 3)
        id = order.id

        order.delete()
        with self.assertRaises(Order.DoesNotExist):
            Order.objects.get(id=id)

    def test_order_limits(self):

        # valid btc value
        order = Order.objects.create(amount=1.00000001, limit=5)
        self.assertEqual(order.amount, 1.00000001)

        # invalid btc value should round to 1
        order.amount = 1.000000001
        order.save()
        order = Order.objects.get(id=order.id)
        self.assertEqual(order.amount, 1)

        order.amount = 1000000
        order.save()
        order = Order.objects.get(id=order.id)
        self.assertEqual(order.amount, 1000000)

        order.amount = 10000000
        with self.assertRaises(InvalidOperation):
            order.save()

    def test_crud_trade(self):
        order_sell = Order.objects.create(limit=5, amount=5)
        order_buy = Order.objects.create(limit=5, amount=5)
        trade = Trade.objects.create(buy_order_id=order_buy.id, sell_order_id=order_sell.id, rate=3.141596)

        # read
        self.assertEqual(trade.buy_order_id, order_buy.id)
        self.assertEqual(trade.sell_order_id, order_sell.id)
        self.assertEqual(trade.rate, 3.141596)
        self.assertEqual(False, trade.filled)

        # update
        trade.sell_order = order_buy
        trade.buy_order = order_sell
        trade.rate = 4
        trade.filled = True
        trade.save()
        trade = Trade.objects.get(id=trade.id)

        # read
        self.assertEqual(trade.buy_order_id, order_sell.id)
        self.assertEqual(trade.sell_order_id, order_buy.id)
        self.assertEqual(trade.rate, 4)
        self.assertEqual(True, trade.filled)
        id = trade.id

        trade.delete()
        with self.assertRaises(Trade.DoesNotExist):
            Trade.objects.get(id=id)

