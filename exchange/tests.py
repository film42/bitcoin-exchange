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