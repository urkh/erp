from django.forms import ModelForm
from django import forms
from modulos.proveedores.models import Proveedores


class FormProveedores(ModelForm):
    class Meta:
        model = Proveedores

