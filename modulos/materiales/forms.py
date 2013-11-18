from django.forms import ModelForm
from django import forms
from modulos.materiales.models import Materiales


class FormMateriales(ModelForm):
    class Meta:
        model = Materiales

