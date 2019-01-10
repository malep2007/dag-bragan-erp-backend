from django.test import TestCase
from customer.models import Inquiry, Customer
from django.contrib.auth.models import User


class TestCustomerModel(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="test", password="passowrd")
        self.login = self.client.login(username='testuser', password='12345')
        self.test_inquiry = Inquiry.objects.create(
            job_type = "Hygiene",
            recorded_by=self.user,
            approve_job = True
        )
        self.test_customer = Customer.objects.create(
            location="test_location",
            first_name="test",
            last_name="customer",
            phone_number="0000",
            inquiry = self.test_inquiry
        )

    def test_user_created(self):
        self.assertTrue(self.user.username, "test")

    def test_customer_created(self):
        self.assertTrue(self.test_customer.first_name, "test")

    def test_inquiry_created(self):
        self.assertTrue(self.test_inquiry, self.test_customer.inquiry)

    def test_can_retrieve_correct_inquiry_data(self):
        self.assertTrue(self.test_inquiry.approve_job, True)
        self.assertIsNot(self.test_inquiry.job_type, "Technical")
