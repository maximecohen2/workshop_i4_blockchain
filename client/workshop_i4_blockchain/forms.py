from django import forms

class ClientForm(forms.Form):
    houseNumber = forms.IntegerField()
    houseStreet = forms.CharField()
    postalCode =forms.IntegerField()
    city = forms.CharField()
    country = forms.CharField()
    lastName = forms.CharField()
    firstName = forms.CharField()
    birthDate = forms.DateField()
    address = forms.NumberField()
    contractNumber = forms.NumberField()
