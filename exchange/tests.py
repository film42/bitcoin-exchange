from django.test import TestCase
from exchange.models import *
from decimal import *
from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse

from model_mommy import mommy
from rest_framework import status
from exchange.models import Order, Trade, Exchange, Account, User
from exchange.models import CurrencyTypes, SideTypes, TradeTypes, FilledStatusTypes


class OrderCRUD(TestCase):

    def test_crud_order(self):
        user = User(username="demo1", email="d1@d.com")
        user.save()

        order = Order.objects.create(amount=5, limit=5, user=user,
                                     from_currency=CurrencyTypes.BTC,
                                     to_currency=CurrencyTypes.USD,
                                     side=SideTypes.BUY,
                                     order_type=TradeTypes.LIMIT)
        self.assertEqual(order.amount, 5)
        self.assertEqual(order.from_currency, CurrencyTypes.BTC)
        self.assertEqual(order.limit, 5)

        #update
        order.amount = 10
        order.limit = 3
        order.save()

        #read
        self.assertEqual(order.amount, 10)
        self.assertEqual(order.limit, 3)
        id = order.id

        order.delete()
        with self.assertRaises(Order.DoesNotExist):
            Order.objects.get(id=id)

    def test_order_limits(self):
        user = User(username="demo", email="d@d.com")
        user.save()

        # valid btc value
        order = Order.objects.create(amount=1.00000001, limit=5, user=user)
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
        user = User(username="demo2", email="d2@d.com")
        user.save()

        order_sell = Order.objects.create(limit=5, amount=5, user=user)
        order_buy = Order.objects.create(limit=5, amount=5, user=user)
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



class EndpointsTestCase(TestCase):
    def generic_get_create_delete(self, list_url, detail_url, mocking_function, expected_id=None):
        not_found = "{\"detail\":\"Not found\"}"
        empty = '[]'

        base_path = reverse(list_url)
        path_one = reverse(detail_url, args=[1])
        path_two = reverse(detail_url, args=[2])

        if expected_id:
            path_one = reverse(detail_url, args=[expected_id])
            path_two = reverse(detail_url, args=[1 if expected_id != 1 else 2])

        client = Client()
        # client.login(username=self.username, password=self.password)
        client.login()

        self.assertEquals(empty, client.get(base_path).content)

        # create an object and get it
        object = mocking_function(self)

        self.assertNotEquals(empty, client.get(base_path).content)
        self.assertEquals(not_found, client.get(path_two).content)
        self.assertNotEquals(not_found, client.get(path_one).content)

        # delete the object and verify that it was deleted
        self.assertEqual(status.HTTP_204_NO_CONTENT, client.delete(path_one).status_code)
        self.assertEquals(not_found, client.get(path_one).content)
        self.assertEqual(status.HTTP_404_NOT_FOUND, client.delete(path_two).status_code)

        # make sure that the collection is empty after the object is deleted
        self.assertEquals(empty, client.get(base_path).content)

    def test_order(self):
        def local_mocking_function(self):
            return mommy.make(Order)

        list_url_local = 'order-list'
        detail_url_local = 'order-detail'

        self.generic_get_create_delete(list_url=list_url_local, detail_url=detail_url_local,
                                       mocking_function=local_mocking_function)

    def test_trade(self):
        def local_mocking_function(self):
            return mommy.make(Trade)

        list_url_local = 'trade-list'
        detail_url_local = 'trade-detail'

        self.generic_get_create_delete(list_url=list_url_local, detail_url=detail_url_local,
                                       mocking_function=local_mocking_function)

    def test_exchange(self):
        def local_mocking_function(self):
            return mommy.make(Exchange)

        list_url_local = 'exchange-list'
        detail_url_local = 'exchange-detail'

        self.generic_get_create_delete(list_url=list_url_local, detail_url=detail_url_local,
                                       mocking_function=local_mocking_function)

    def test_account(self):
        def local_mocking_function(self):
            return mommy.make(Account)

        list_url_local = 'account-list'
        detail_url_local = 'account-detail'

        self.generic_get_create_delete(list_url=list_url_local, detail_url=detail_url_local,
                                       mocking_function=local_mocking_function)
