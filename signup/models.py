from django.db import models
import datetime
from datetime import timedelta

class DonorInfo(models.Model):
    name = models.CharField(max_length=35)
    street_address = models.CharField(blank=True, null=True, max_length=50)
    city = models.CharField(max_length=25, blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    zipcode = models.IntegerField(null=True)
    email = models.EmailField(max_length=35, blank=True, null=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    date_created = models.DateTimeField(default=datetime.datetime.now, null=True)
    payment_recvd = models.NullBooleanField(null=True, blank=True)
    date_recvd = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name
