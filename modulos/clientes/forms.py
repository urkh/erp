from django.forms import ModelForm
from django import forms
from modulos.clientes.models import Clientes


class FormClientes(ModelForm):
    class Meta:
        model = Clientes

