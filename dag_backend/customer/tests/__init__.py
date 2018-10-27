from  django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from customer.models import Customer, Inquiry

class BaseTestCase(TestCase):
    """
    Base setup for test case
    """

    def setUp(self):
        self.client = APIClient()
        self.reg_data = {
            "user":{
                "username": "test_user",
                "email": "test@test.com",
                "password": "password"
            }
        }

        self.client_data = {
            "customer":{
                "business_name": "Andela Uganda",
                "location": "somewhere",
                "first_name": "test",
                "last_name": "user",
                "middle_name": "",
                "phone_number": "12345",
                "inquiry": 1
            }
        }

        self.inquiry_data = {
            "inquiry": {
                "id": 1,
                "recorded_by": 1,
                "inspection_date": "2018-10-20",
                "extra_details": "Bed bug infestations",
                "date_created": "2018-10-20T07:14:02.071897Z",
                "inq_number": "INQ/2018/10/20/1",
                "approve_job": True
            }
        }

    def __init__(self, *args, **kwargs):
        self.setUp()
