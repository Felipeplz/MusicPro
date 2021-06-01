from django.shortcuts import render
from musicpro.models import SQLProductos
import pyodbc

# Create your views here.
def productosTodos(request):
    conn = pyodbc.connect('Driver={sql server};'
                        'Server=LAPTOP-O114NIEM;'
                        'Database=MusicPro;'
            
                        'Trusted_Connection=yes')
    cursor = conn.cursor()
    result = cursor.execute("SELECT * FROM PRODUCTO ORDER BY id_producto ASC").fetchall()
    return render(request, 'Catalogo_Producto.html', {'SQLProductos':result})

def Registro(request):
    return render(request, 'Registro.html',)