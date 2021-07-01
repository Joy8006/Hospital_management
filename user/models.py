from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timesince, timezone


class UserAccount(AbstractUser):
    """Custom user model for our system"""
    
    country = models.CharField(max_length=40, blank=True, null=True)
    phone = models.CharField(blank=True, null=True, max_length=15)
    hospital = models.ForeignKey('hospital.Hospital', on_delete=models.SET_NULL, null=True)
    date_of_birth = models.DateField(blank=True, null=True)

    @property
    def full_name(self):
        name = self.get_full_name() or self.username
        return name

    @property
    def age(self):
        if self.date_of_birth:
            return timesince.timesince(self.date_of_birth, timezone.datetime.today())
        return 0