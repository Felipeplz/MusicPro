from django.http import response, HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from musicpro.models import SQLDespachos,SQLEstadoPedidos,SQLItemVentas,SQLPagos,SQLProductos,SQLPromociones,SQLSucursales,SQLUsuarios,SQLVentas
from .conn import *
from django.http.response import JsonResponse
import pyodbc
import transbank

conn = pyodbc.connect('Driver={ODBC Driver 17 for Sql Server};'
                      'Server=RENO-PC\SQLEXPRESS;'
                      'Database=MusicPro;'
                      'Trusted_Connection=yes')

def Conectar():
    return conn.cursor()

def setCookie(request, nombre, valor):
    request.set_cookie(nombre, valor)
    return request

def getCookie(request, nombre):
    resultado = request.COOKIES.get(nombre, 0)
    return resultado