from .conn import *

def viewProducto(request, **kwargs):
    id = kwargs.get('id')
    result = Conectar().execute(f"SELECT nombre AS NombreProd, foto AS FotoProd, descripcion AS DescripcionProd, COUNT(id_producto) AS CantidadProd, precio AS PrecioProd FROM PRODUCTO GROUP BY nombre, foto, descripcion, precio;").fetchone()
    return render(request, 'productosDetalle.html', {'SQLProdDetalle':result})
