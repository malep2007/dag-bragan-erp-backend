from django.db import models
from django.contrib.auth.models import User

import datetime


class Customer(models.Model):
    business_name = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=100, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=12)

    def __str__(self):
        """check for name that exists and return that name"""
        self.name = "{0} {1}".format(self.first_name, self.last_name)
        if self.business_name:
            return self.business_name
        else:
            return self.name


class Inquiry(models.Model):
    JOB_TYPES = (
        ('H', 'Hygiene'),
        ('T', 'Technical')
    )

    @staticmethod
    def generate_inquiry_number(self):
        time = datetime.datetime.now()
        return "INQ/{0}/{1}/{2}".format(
            time.year, time.month, time.date
        )

    name = models.ForeignKey(Customer, models.CASCADE)
    job_type = models.CharField(
        max_length=20,
        choices=JOB_TYPES,
        default="Hygiene"
    )
    recorded_by = models.ForeignKey(User, models.CASCADE)
    inspection_date = models.DateField(null=True)
    extra_details = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    inq_number = models.CharField(
        max_length=20,
        default='generate_inquiry_number',
        editable=False
    )

    def __str__(self):
        return "{}".format(self.inq_number)
