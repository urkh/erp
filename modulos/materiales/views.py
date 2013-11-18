from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from modulos.materiales.models import Materiales
from modulos.materiales.forms import FormMateriales



def material(request, id):
    material = Materiales.objects.get(id=id)
    return render_to_response('material.html', {'material':material})


def materiales(request):
    materiales = Materiales.objects.all()
    return render_to_response('materiales.html', {'materiales':materiales})


def nuevo_material(request):
    if request.method=='POST':
        form = FormMateriales(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/materiales/')
    else:
        form = FormMateriales()

    return render_to_response('add_material.html', {'form':form})





