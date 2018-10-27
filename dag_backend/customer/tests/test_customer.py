from rest_framework import status
from django.test import TestCase
from customer.tests import BaseTestCase

class TestCustomer(BaseTestCase, TestCase):
    def test_can_get_client_list(self):
        response = self.client.get("/customer/", self.client_data)
        return self.assertEquals(response.status_code, status.HTTP_200_OK)
