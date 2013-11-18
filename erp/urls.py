from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    

    url(r'^$', 'modulos.dashboard.views.dashboard'),

    url(r'^clientes/$', 'modulos.clientes.views.clientes'),
    url(r'^clientes/(\d+)/$', 'modulos.clientes.views.cliente'),
    url(r'^clientes/nuevo/$', 'modulos.clientes.views.nuevo_cliente'),
    
    url(r'^articulos/$', 'modulos.articulos.views.articulos'),
    url(r'^articulos/(\d+)/$', 'modulos.articulos.views.articulo'),
    url(r'^articulos/nuevo/$', 'modulos.articulos.views.nuevo_articulo'),

    url(r'^proveedores/$', 'modulos.proveedores.views.proveedores'),
    url(r'^proveedores/(\d+)/$', 'modulos.proveedores.views.proveedor'),
    url(r'^proveedores/nuevo/$', 'modulos.proveedores.views.nuevo_proveedor'),   

    url(r'^ventas/$', 'modulos.ventas.views.ventas'),
    url(r'^ventas/(\d+)/$', 'modulos.ventas.views.venta'),
    url(r'^ventas/nuevo/$', 'modulos.ventas.views.nuevo_venta'),   

    url(r'^pedidos/$', 'modulos.pedidos.views.pedidos'),
    url(r'^pedidos/(\d+)/$', 'modulos.pedidos.views.pedido'),
    url(r'^pedidos/nuevo/$', 'modulos.pedidos.views.nuevo_pedido'),   
    
    #url(r'^estadisticas/$', 'modulos.estadisticas.views.estadisticas'),
    #url(r'^estadisticas/(+d)/$', 'modulos.estadisticas.views.estadistica'),
    #url(r'^estadisticas/nuevo/$', 'modulos.estadisticas.views.nuevo_estadistica'),   

    url(r'^materiales/$', 'modulos.materiales.views.materiales'),
    url(r'^materiales/(\d+)/$', 'modulos.materiales.views.material'),
    url(r'^materiales/nuevo/$', 'modulos.materiales.views.nuevo_material'),   


    url(r'^admin/', include(admin.site.urls)),
)
