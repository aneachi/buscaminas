from django import forms

class CreaTableroForm(forms.Form):
    filas = forms.IntegerField(label='Filas', max_value=20, min_value=1, initial=2)
    columnas = forms.IntegerField(label='Columnas', max_value=15, min_value=1, initial=2)