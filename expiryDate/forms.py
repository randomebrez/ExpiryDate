from django import forms
from datetime import date

class RefForm(forms.Form):
    reference = forms.IntegerField(label = 'Réference')

class AjoutForm(forms.Form):
    reference = forms.IntegerField(label = 'Référence')
    date = forms.DateField(initial=date.today)

