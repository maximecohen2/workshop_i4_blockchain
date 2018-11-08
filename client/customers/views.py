from django.shortcuts import render
from client.customers.models import *

def getPersonByCommune(commune):
    customers = Customer.objects.all().filter(address__city__contains=commune)
    return customers

def getContratByPersonne(personne):
    contrat = Contract.objects.filter(customer=personne)
    return contrat

def getAddressByPersonne(personne):
    address = Address.objects.filter(customer=personne)
    return address
