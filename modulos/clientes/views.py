from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from modulos.clientes.models import Clientes
from modulos.clientes.forms import FormClientes



def cliente(request, id):
    cliente = Clientes.objects.get(id=id)

    if request.method=='POST':
        form = FormClientes(request.POST, instance=cliente)
        if form.is_valid():

            cliente = form.save(commit=False)
            cliente.id = request.id
            cliente.save()
            #form.save()
            return HttpResponseRedirect('/clientes/')
    else:
        form = FormClientes()

    return render_to_response('cliente.html', {'cliente':cliente}, context_instance=RequestContext(request))


def clientes(request):
    clientes = Clientes.objects.all()
    return render_to_response('clientes.html',{'clientes': clientes})


def nuevo_cliente(request):
    
    if request.method=='POST':
        form = FormClientes(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/clientes/')
    else:
        form = FormClientes()
    
    return render_to_response('add_cliente.html', {'form': form}, context_instance=RequestContext(request))

