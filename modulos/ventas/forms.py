from django.forms import ModelForm
from django import forms
from modulos.ventas.models import Ventas


class FormVentas(ModelForm):
    class Meta:
        model = Ventas

