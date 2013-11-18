from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from modulos.ventas.models import Ventas
from modulos.ventas.forms import FormVentas



def venta(request, id):
    venta = Ventas.objects.get(id=id)
    return render_to_response('venta.html', {'venta':venta})


def ventas(request):
    ventas = Ventas.objects.all()
    return render_to_response('ventas.html', {'ventas':ventas})


def nuevo_venta(request):
    if request.method=='POST':
        form = FormVentas(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/ventas/')
    else:
        form = FormVentas()

    return render_to_response('add_venta.html', {'form':form})





