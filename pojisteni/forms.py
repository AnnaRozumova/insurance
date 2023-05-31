from django import forms
from pojisteni.models import Pojistence, Pojisteni, Uzivatel

class PojistenceForm(forms.ModelForm):

    class Meta:
        model = Pojistence
        fields=['jmeno', 'prijmeni', 'email', 'telefon', 'adresa']


class PojisteniForm(forms.ModelForm):

    class Meta:
        model = Pojisteni
        fields = ['id_pojistence', 'nazev', 'predmet', 'platnost_od', 'platnost_do', 'pojistna_osoba']

class UzivatelForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput)
    class Meta:
        model = Uzivatel
        fields = ['email', 'password']

class LoginForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        fields = ['email', 'password']