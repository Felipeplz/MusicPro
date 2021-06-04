from .conn import *

def seguimientoBodeguero(request):
    result = Conectar().execute("SELECT V.id_venta, IV.cantidad, U.nombre, P.tipo, EP.fecha_estado,EP.estado FROM VENTA V JOIN USUARIO U ON U.id_usuario = V.id_cliente JOIN ESTADO_PEDIDO EP ON EP.id_venta = V.id_venta JOIN ITEM_VENTA IV ON V.id_venta = IV.id_venta JOIN PRODUCTO P ON IV.id_producto = P.id_producto ORDER BY V.id_venta ASC").fetchall()
    return render(request, 'seguimientoBodeguero.html', {'SQLBodeguero':result})

# def seguimientoBodeguero2(request):
    # result = Conectar().execute("SELECT V.id_venta, IV.cantidad, U.nombre, P.tipo, EP.fecha_estado,EP.estado FROM VENTA V JOIN USUARIO U ON U.id_usuario = V.id_cliente JOIN ESTADO_PEDIDO EP ON EP.id_venta = V.id_venta JOIN ITEM_VENTA IV ON V.id_venta = IV.id_venta JOIN PRODUCTO P ON IV.id_producto = P.id_producto WHERE U.nombre = 'ELNOMBRE DEL USUARIO' ORDER BY U.nombre ASC").fetchall()
    # return render(request, 'Seguimiento_bodeguero_mis_pedidos.html', {'SQLBodeguero2':result})