from .conn import *

def seguimientoBodeguero(request,**kwargs):
    tab = kwargs.get('tab')
    if (tab == None):
        tab = "todos"
        query = ""
    else:
        query = f"WHERE U.id_usuario = '{tab}'"
    result = Conectar().execute(f"SELECT V.id_venta, IV.cantidad, U.nombre, P.tipo, EP.fecha_estado,EP.estado,CONVERT(time(0),ep.fecha_estado) AS HORA FROM VENTA V JOIN USUARIO U ON U.id_usuario = V.id_cliente JOIN ESTADO_PEDIDO EP ON EP.id_venta = V.id_venta JOIN ITEM_VENTA IV ON V.id_venta = IV.id_venta JOIN PRODUCTO P ON IV.id_producto = P.id_producto {query} ORDER BY V.id_venta ASC").fetchall()
    return render(request, 'seguimientoBodeguero.html', {'SQLBodeguero':result, 'tab':tab})

