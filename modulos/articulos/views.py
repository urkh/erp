from django.shortcuts import render_to_response
#from django.template import RequestContext

# Create your views here.


def articulos(request):
    return render_to_response('articulos.html')

