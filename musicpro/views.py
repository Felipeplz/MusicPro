from django.shortcuts import render
from musicpro.models import SQLProductos
import pyodbc

# Create your views here.
def productosTodos(request):
    conn = pyodbc.connect('Driver={sql server};'
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