from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from modulos.proveedores.models import Proveedores
from modulos.proveedores.forms import FormProveedores



def proveedor(request, id):
    proveedor = Proveedores.objects.get(id=id)
    return render_to_response('proveedor.html', {'proveedor':proveedor})


def proveedores(request):
    proveedores = Proveedores.objects.all()
    return render_to_response('proveedores.html', {'proveedores':proveedores})


def nuevo_proveedor(request):
    if request.method=='POST':
        form = FormProveedores(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/proveedores/')
    else:
        form = FormProveedores()

    return render_to_response('add_proveedor.html', {'form':form})





