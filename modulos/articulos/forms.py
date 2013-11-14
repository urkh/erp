from django.forms import ModelForm
from django import forms
from modulos.articulos.models import Articulos

class FormArticulos(ModelForm):
    class Meta:
        model = Articulos
