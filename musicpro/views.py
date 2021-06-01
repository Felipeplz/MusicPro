from django.shortcuts import render
from musicpro.models import SQLProductos, SQLVentas
import pyodbc

# Create your views here.
def productosTodos(request):
    conn = pyodbc.connect('Driver={sql server};'
                        'Server=DESKTOP-T62UH2C;'
                        'Database=MusicPro;'
                        'Trusted_Connection=yes')
    cursor = conn.cursor()
    result = cursor.execute("SELECT * FROM PRODUCTO ORDER BY id_producto ASC").fetchall()
    return render(request, 'Catalogo_Producto.html', {'SQLProductos':result})

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