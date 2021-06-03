from django.shortcuts import render
from musicpro.models import SQLProductos
import pyodbc

# Create your views here.

def Conectar():
    conn = pyodbc.connect('Driver={sql server};'
                        'Server=LAPTOP-O114NIEM;'
                        'Database=MusicPro;'
                        'UID=django-user;'
                        'PWD=%.ZSix:)R:NN5RT')
    return conn.cursor()

def viewCatalogo(request, **kwargs):
    if (request.path == "/"):
        return redirect('/catalogo')
    tab = kwargs.get('tab')
    if (tab == None):
        tab = "todos"
        query = ""
    else:
        query = f"WHERE categoria = '{tab}'"
    result = Conectar().execute(f"SELECT * FROM PRODUCTO {query} ORDER BY id_producto ASC").fetchall()
    return render(request, 'Catalogo_Producto.html', {'SQLProductos':result, 'tab': tab})
