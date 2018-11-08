from django import forms

class InscriptionForm(forms.Form):
    CHOICES = (
        ('Mr','MR'),
        ('Mme', 'MME'),
        ('Mlle', 'MLLE'),
    )
    civilite = forms.ChoiceField(choices=CHOICES)
    firstName = forms.CharField(max_length=128, label="Nom")
    lastName = forms.CharField(max_length=128, label="Prénom")
    postalCode = forms.CharField(max_length=5, label="Code Postal")
    city = forms.CharField(max_length=128, label="Ville")
    email = forms.EmailField(max_length=128, label="Email")
    contractNumber = forms.CharField(max_length=15, label="N° de contrat")
    cgu = forms.BooleanField(label="J'accepte que mes données personnelles soient \
    utilisées pour être recontacté par AXA à des fins commerciales", required=False)
