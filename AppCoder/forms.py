from tabnanny import verbose
from django import forms

class NuevoDeporte(forms.Form):
    nombre = forms.CharField(max_length='30')
    precio = forms.IntegerField(min_value='0')