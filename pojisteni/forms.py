from django import forms
from pojisteni.models import Pojistence, Pojisteni

class PojistenceForm(forms.ModelForm):

    class Meta:
        model = Pojistence
        fields=['jmeno', 'prijmeni', 'email', 'telefon', 'adresa']


class PojisteniForm(forms.ModelForm):

    class Meta:
        model = Pojisteni
        fields = ['id_pojistence', 'nazev', 'predmet', 'platnost_od', 'platnost_do', 'pojistna_osoba']