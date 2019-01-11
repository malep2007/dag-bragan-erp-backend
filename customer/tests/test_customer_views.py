from django.test import TestCase, Client
from django.urls import reverse


class TestCustomerView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_customer_list_view_works(self):
        self.response = self.client.get(reverse('customer:index'))
        self.assertTrue(self.response.status_code, 200)





