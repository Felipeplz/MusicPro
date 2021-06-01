from django.shortcuts import redirect, render
from musicpro.models import SQLProductos
import pyodbc

# Create your views here.
def viewCatalogo(request, **kwargs):
    if (request.path == "/"):
        return redirect('/catalogo')
    conn = pyodbc.connect('Driver={sql server};'
                        'Server=FELIPE-LEGION\FELIPE;'
                        'Database=MusicPro;'
                        'UID=django-user;'
                        'PWD=%.ZSix:)R:NN5RT')
    cursor = conn.cursor()
    tab = kwargs.get('tab')
    if (tab == None):
        tab = "todos"
        query = ""
    else:
        query = f"WHERE categoria = '{tab}'"
    result = cursor.execute(f"SELECT * FROM PRODUCTO {query} ORDER BY id_producto ASC").fetchall()
    return render(request, 'Catalogo_Producto.html', {'SQLProductos':result, 'tab': tab})