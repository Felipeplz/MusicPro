from .conn import *

def productosCarrito(request):
    result = Conectar().execute("SELECT * FROM PRODUCTO ORDER BY id_producto ASC").fetchall()
    return render(request, 'carrito.html', {'SQLCarrito':result})