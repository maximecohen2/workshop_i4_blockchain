from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

class Address(models.Model):
    houseNumber = models.IntegerField(validators=[MinValueValidator(1)], null=True)
    houseStreet = models.CharField(max_length=255, null=True)
    postalCode = models.CharField(max_length=10)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255, null=True)

class Customer(models.Model):
    civilite = models.CharField(max_length=5)
    lastName = models.CharField(max_length=128)
    firstName = models.CharField(max_length=128)
    birthDate = models.DateField(null=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True)

class Contract(models.Model):
    contractNumber = models.CharField(max_length=30)
