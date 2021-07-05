from .conn import *
from musicpro.serializers import UsuarioSerializer
from rest_framework import viewsets
from musicpro.serializers import ProductoSerializer
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

@api_view(['POST'])
def loginRest(request):
  username = request.POST.get('username')
  password = request.POST.get('password')

  try:
    user = User.objects.get(username=username)
  except User.DoesNotExist:
    return Response("Usuario y/o contraseña inválidos")

  pwdValid = check_password(password, user.password)

  if not pwdValid:
    return Response("Usuario y/o contraseña inválidos")

  token, created = Token.objects.get_or_create(user=user)

  print(token.key)
  return Response(token.key)

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        productos = Producto.objects.all()

        id_producto = self.request.GET.get('id')
        nombre = self.request.GET.get('nombre')
        marca = self.request.GET.get('marca')
        tipo = self.request.GET.get('tipo')
        subtipo = self.request.GET.get('subtipo')
        categoria = self.request.GET.get('categoria')
        descripcion = self.request.GET.get('descripcion')
        
        if id_producto:
            productos = productos.filter(id=id_producto)
        if nombre:
            productos = productos.filter(nombre__contains=nombre.encode().decode('utf-8'))
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
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer