from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

class Address(models.Model):
    houseNumber = models.IntegerField(validators=[MinValueValidator(1)])
    houseStreet = models.CharField(max_length=255)
    postalCode = models.CharField(max_length=10)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

class Customer(models.Model):
    lastName = models.CharField(max_length=128)
    firstName = models.CharField(max_length=128)
    birthDate = models.DateField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

class Contract(models.Model):
    customer = models.OneToOneField(
        Customer,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    contractNumber = models.CharField(max_length=30)
