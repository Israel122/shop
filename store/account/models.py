from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Person(AbstractUser):
    is_verified = models.BooleanField(default=False)


class Address(models.Model):
    description = models.TextField()
    country = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    addressType = models.CharField(max_length=200)
    person = models.ForeignKey(Person, on_delete=models.DO_NOTHING)


class Payment(models.Model):
    cardNumber = models.CharField(max_length=20)
    cardPin = models.IntegerField(max_length=4)
    expiryDate = models.DateField()
    cardCode = models.IntegerField()
    person = models.ForeignKey(Person, on_delete=models.DO_NOTHING)
