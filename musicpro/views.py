from django.shortcuts import redirect, render
from musicpro.models import SQLProductos
import pyodbc

# Create your views here.

def Conectar():
    conn = pyodbc.connect('Driver={sql server};'
<<<<<<< HEAD
                         'Server=LAPTOP-R0CJDD69\PIA;'
                         'Database=MusicPro;'
                        'Trusted_Connection=yes')
    cursor = conn.cursor()
    result = cursor.execute("SELECT * FROM PRODUCTO ORDER BY id_producto ASC").fetchall()
    return render(request, 'Catalogo_Producto.html', {'SQLProductos':result})

def detalleProducto(request):
    conn = pyodbc.connect('Driver={sql server};'
                         'Server=LAPTOP-R0CJDD69\PIA;'
                         'Database=MusicPro;'
                        'Trusted_Connection=yes')
    cursor = conn.cursor()
    result = cursor.execute("SELECT * FROM PRODUCTO ORDER BY id_producto ASC").fetchall()
    return render(request, 'Detalle_Producto.html', {'SQLProductos':result})
=======
                        'Server=FELIPE-LEGION\FELIPE;'
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
>>>>>>> fd375f9acadac3178a250713a99d60304cb04946
