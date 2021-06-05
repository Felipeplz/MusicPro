from .conn import *

def viewproductosLista(request, **kwargs):
    id = kwargs.get('id')
    result = Conectar().execute("SELECT * FROM PRODUCTO").fetchall()
    return render(request, 'productosLista.html', {'SQLProducto':result})