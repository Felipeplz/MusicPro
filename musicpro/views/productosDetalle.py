from .conn import *

def viewProducto(request, **kwargs):
    id = kwargs.get('id')
    result = Conectar().execute("SELECT * "
                            "FROM PRODUCTO "
                            f"WHERE id_producto = {id}").fetchone()
    return render(request, 'productosDetalle.html', {'SQLPromo':result})