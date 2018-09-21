from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
import datetime
class DonorInfo(models.Model):
    name = models.CharField(max_length=35)
    street_address = models.CharField(blank=True, null=True, max_length=50)
    city = models.CharField(max_length=25, blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    zipcode = models.IntegerField(null=True)
    email = models.EmailField(max_length=35, blank=True, null=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    date_created = models.DateTimeField(default=datetime.datetime.now, null=True)

    def __str__(self):
        return self.name


@receiver(post_save, sender=DonorInfo)
def create_account(sender, **kwargs):
    if kwargs.get('created', False):
        DonorAccount.objects.get_or_create(name=kwargs.get('instance'))
        DonorAccount.objects.get_or_create(date_created=kwargs.get('instance'))
class DonorAccount(models.Model):
    name = models.OneToOneField(DonorInfo, related_name='donorname', on_delete=models.CASCADE)
    amount_paid = models.IntegerField(null=True)
    date_created = models.OneToOneField(DonorInfo, related_name='datecreated', on_delete='models.CASCADE')
    days_since_created = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return self.name
