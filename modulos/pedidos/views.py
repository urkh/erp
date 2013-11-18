from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from modulos.pedidos.models import Pedidos
from modulos.pedidos.forms import FormPedidos



def pedido(request, id):
    pedido = Pedidos.objects.get(id=id)
    return render_to_response('pedido.html', {'pedido':pedido})


def pedidos(request):
    pedidos = Pedidos.objects.all()
    return render_to_response('pedidos.html', {'pedidos':pedidos})


def nuevo_pedido(request):
    if request.method=='POST':
        form = FormPedidos(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/pedidos/')
    else:
        form = FormPedidos()

    return render_to_response('add_pedido.html', {'form':form})





