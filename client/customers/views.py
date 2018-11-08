from django.shortcuts import render
from customers.models import *
from .form import InscriptionForm


def inscription(request):
    form = InscriptionForm(None)
    return render(request, 'inscription.html', locals())

def success(request):
    form = InscriptionForm(request.POST)
    if form.is_valid():
        customer = Customer()
        address = Address()
        contract = Contract()

        customer.civilite = form.cleaned_data['civilite']
        customer.lastName = form.cleaned_data['lastName']
        customer.firstName = form.cleaned_data['firstName']

        address.postalCode = form.cleaned_data['postalCode']
        address.city = form.cleaned_data['city']

        contract.contractNumber = form.cleaned_data['contractNumber']
        
        customer.save()
        address.save()
        contract.save()
        
    return render(request, 'success.html', locals())

def getPersonByCommune(commune):
    customers = Customer.objects.all().filter(address__city__contains=commune)
    return customers

def getContratByPersonne(personne):
    contrat = Contract.objects.filter(customer=personne)
    return contrat

def getAddressByPersonne(personne):
    address = Address.objects.filter(customer=personne)
    return address
