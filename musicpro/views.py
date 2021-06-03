from django.shortcuts import redirect, render
from musicpro.models import SQLProductos, SQLVentas
import pyodbc

# Create your views here.

def Conectar():
    conn = pyodbc.connect('Driver={sql server};'
                        'Server=DESKTOP-T62UH2C;'
                        'Database=MusicPro;'
                        'Trusted_Connection=yes')
    return conn.cursor()

def ventastodos(request):
    conn = pyodbc.connect('Driver={sql server};'
                        'Server=DESKTOP-T62UH2C;'
                        'Database=MusicPro;'
                        'Trusted_Connection=yes')
    cursor = conn.cursor()
    result = cursor.execute("SELECT * FROM VENTA ORDER BY id_venta ASC").fetchall()
    return render(request, 'ReporteVentas.html', {'SQLVentas':result})

def ventastodos(request):
    conn = pyodbc.connect('Driver={sql server};'
                        'Server=DESKTOP-T62UH2C;'
                        'Database=MusicPro;'
                        'Trusted_Connection=yes')
    cursor = conn.cursor()
    result = cursor.execute("SELECT * FROM VENTA ORDER BY id_venta ASC").fetchall()
    return render(request, 'ReporteVentas.html', {'SQLVentas':result})
    
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
