from django.contrib import admin
from customers.models import Customer, Address, Contract

# Register your models here.
admin.site.register(Customer)
admin.site.register(Address)
admin.site.register(Contract)
