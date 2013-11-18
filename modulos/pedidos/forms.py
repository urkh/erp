from django.forms import ModelForm
from django import forms
from modulos.pedidos.models import Pedidos


class FormPedidos(ModelForm):
    class Meta:
        model = Pedidos

