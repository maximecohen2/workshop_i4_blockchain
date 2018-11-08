from django.shortcuts import render
from customers.models import *
from .form import InscriptionForm

def inscription(request):
    form = InscriptionForm(request.POST or None)
    if form.is_valid():
        civilite = form.cleaned_data['civilite']
    return render(request, 'inscription.html', locals())

def success(request):
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
