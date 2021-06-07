from .conn import *
from musicpro.serializers import UsuarioSerializer
from rest_framework import viewsets
from musicpro.serializers import ProductoSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = SQLProductos.objects.all()
    serializer_class = ProductoSerializer

    def get_queryset(self):
        productos = SQLProductos.objects.all()
        print(list(productos.values()))

        id_producto = self.request.GET.get('id_producto')
        codigo_producto = self.request.GET.get('codigo_producto')
        nombre = self.request.GET.get('nombre')
        marca = self.request.GET.get('marca')
        tipo = self.request.GET.get('tipo')
        subtipo = self.request.GET.get('subtipo')
        categoria = self.request.GET.get('categoria')
        descripcion = self.request.GET.get('descripcion')
        if id_producto:
            productos = productos.filter(id_producto=id_producto)
        if codigo_producto:
            productos = productos.filter(codigo_producto__contains=codigo_producto)
        if nombre:
            productos = productos.filter(nombre__contains=nombre)
        if marca:
            productos = productos.filter(marca__contains=marca)
        if tipo:
            productos = productos.filter(tipo__contains=tipo)
        if subtipo:
            productos = productos.filter(subtipo__contains=subtipo)
        if categoria:
            productos = productos.filter(categoria__contains=categoria)
        if descripcion:
            productos = productos.filter(descripcion__contains=descripcion)

        return productos

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = SQLUsuarios.objects.all()
    serializer_class = UsuarioSerializer