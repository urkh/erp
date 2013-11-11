from django.forms import ModelForm
from django import forms
from clientes.models import Clientes


class ClientesForm(ModelForm):
    class Meta:
        model = Clientes

