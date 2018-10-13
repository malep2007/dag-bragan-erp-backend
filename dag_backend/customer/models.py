from django.db import models
from django.contrib.auth.models import User
from django.utils.deconstruct import deconstructible

import datetime

class Inquiry(models.Model):
    JOB_TYPES = (
        ('H', 'Hygiene'),
        ('T', 'Technical')
    )

    @property
    def gen_inq_number(self):
        time = datetime.datetime.now()
        self.inq_number = "INQ/{}/{}/{}/{}".format(time.year, time.month, time.day, self.id)
        inq = Inquiry.objects.get(id=self.id)
        inq.inq_number = self.inq_number
        inq.save()
        return self.inq_number


    # customer_name = models.ForeignKey(Customer, models.CASCADE)
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
        editable=False,
        null=True,
    )
    approve_job = models.BooleanField(default=False, null=True)



    def __str__(self):
        return "{}".format(self.gen_inq_number)


class Customer(models.Model):
    business_name = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=100, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=12)
    inquiry = models.OneToOneField(Inquiry, models.CASCADE, null=True, editable=False)

    @property
    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def __str__(self):
        """check for name that exists and return that name"""
        if self.business_name:
            return self.business_name
        else:
            return self.full_name


