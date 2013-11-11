from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from modulos.clientes.models import Clientes
from modulos.clientes.forms import ClientesForm



def cliente(request, id):
    cliente = Clientes.objects.get(id=id)
    return render_to_response('cliente.html', {'cliente':cliente})


def clientes(request):
    clientes = Clientes.objects.all()
    return render_to_response('clientes.html',{'clientes': clientes})


def cliente_nuevo(request):
    if request.method=='POST':
        form = ClientesForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/clientes/lista')
   
    else:
        form = ClientesForm()
    
    return render_to_response('clientesForm.html', {'form': form})

