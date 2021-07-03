from django.http import response, HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.core.files.storage import FileSystemStorage
from musicpro.models import Despacho,Estado,ItemVenta,Pago,Producto,Sucursal,Usuario,Venta
from django.http.response import JsonResponse
from .barraMenu import login
import transbank

# conn = pyodbc.connect('Driver={ODBC Driver 17 for Sql Server};'
#                       'Server=FELIPE-LEGION\FELIPE;'
#                       'Database=MusicPro;'
#                       'Trusted_Connection=yes')

# def Conectar():
#     return conn.cursor()

def getUsuario(mail):
    user = Usuario.objects.get(mail=mail)
    return user

def setCookie(request, nombre, valor):
    request.set_cookie(nombre, valor)
    return request

def getCookie(request, nombre):
    resultado = request.COOKIES.get(nombre, 0)
    return resultado

def checkLogin(request):
    if not request.user.is_authenticated:
        return login(request)