"""musicpro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from musicpro.views.seguimientoCliente import seguimientoCliente
from os import name
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers

router = routers.DefaultRouter()
router.register('producto', views.ProductoViewSet)
router.register('usuario', views.UsuarioViewSet)

urlpatterns = [
    path('', views.viewCatalogo, name='catalogo'),
    path('admin/', admin.site.urls, name=('admin')),
    path('producto/', views.viewProducto, name='producto'),
    path('producto/<int:id>/', views.viewProducto, name='productoid'),
    path('producto/nuevo/', views.newProducto, name='nuevoproducto'),
    path('producto/<int:id>/editar/', views.editProducto, name='editarproducto'),
    path('reporteVentas', views.viewVentas),
    path('productosLista/', views.viewProductosLista),
    path('usuariosLista/', views.viewUsuariosLista),
    path('usuario/nuevo/', views.newUsuario),
    path('usuario/<int:id>/', views.viewUsuario),
    path('usuario/<int:id>/editar/', views.editUsuario),
    path('reporteriaVentas', views.viewVentas),
    path('registro/', views.Registro),
    path('catalogo/', views.viewCatalogo),
    path('catalogo/<str:tab>', views.viewCatalogo),
    path('seguimientoBodeguero/<str:tab>', views.seguimientoBodeguero),
    path('seguimientoCliente/<int:id>', views.seguimientoCliente),
    # path('mispedidos/', views.seguimientoBodeguero2),
    path('promociones/', views.promociones),
    path('carrito/', views.productosCarrito),
    path('carrito/add/', views.anniadirCarrito),
    path('carrito/remove/', views.quitarCarrito),
    path('carrito/edit/', views.cambiarCarrito),
    path('ventasDatos/', views.ventasDatos),
    #path('pagar/<str:total>/', views.validarPago),
    path('api/', include(router.urls)),
    
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)