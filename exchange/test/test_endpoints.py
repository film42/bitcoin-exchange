from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse

from model_mommy import mommy
from rest_framework import status
from exchange.models import Order, Trade, Exchange, Account


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