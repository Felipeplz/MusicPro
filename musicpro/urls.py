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
from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('detalleproducto/', views.detalleProducto),
    path('', views.viewCatalogo),
    path('admin/', admin.site.urls),
    path('ReporteVentas', views.ventastodos),
    path('Registro/', views.Registro),
    path('catalogo', views.viewCatalogo),
    path('catalogo/<str:tab>', views.viewCatalogo),
    # path('pedidosgenerales/', views.seguimientoBodeguero),
    # path('mispedidos/', views.seguimientoBodeguero2),
    path('promociones/', views.promociones),
    path('usuarioslista/', views.viewUsuarios),
    #path('carrito/', views.productosCarrito),
    #path('admin/', admin.site.urls)
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)