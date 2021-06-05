from .conn import *

def viewProducto(request, **kwargs):
    id = kwargs.get('id')
    result = Conectar().execute(f"SELECT *"
                            "FROM PRODUCTO"
                            "WHERE id_producto = {id}").fetchone()
    return render(request, 'productosDetalle.html', {'SQLPromo':result})

   