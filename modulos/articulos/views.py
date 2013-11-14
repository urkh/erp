from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from modulos.articulos.models import Articulos
from modulos.articulos.forms import FormArticulos



def articulo(request, id):
    articulo = Articulos.objects.get(id=id)
    return render_to_response('articulo.html', {'articulo':articulo})


def articulos(request):
    articulos = Articulos.objects.all()
    return render_to_response('articulos.html', {'articulos':articulos})


def nuevo_articulo(request):
    if request.method=='POST':
        form = FormArticulos(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/articulos/')
    else:
        form = FormArticulos()

    return render_to_response('add_articulo.html', {'form':form})





