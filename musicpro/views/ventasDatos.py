from .conn import *
from datetime import datetime
import transbank
id_user = 5

def ventasDatos(request):
    local = getLocale(request)
    result = Conectar().execute("SELECT [dbo].[PRODUCTO].id_producto, [dbo].[PRODUCTO].foto, [dbo].[PRODUCTO].nombre, [dbo].[PRODUCTO].descripcion, [dbo].[PRODUCTO].precio, [dbo].[PRODUCTO].stock, ISNULL([dbo].[VENTA].total, 0) AS total, ISNULL([dbo].[VENTA].descuento, 0) * -1 AS descuento, [dbo].[ITEM_VENTA].cantidad AS cantidad,(ISNULL([dbo].[PRODUCTO].precio,0)-((ISNULL([dbo].[VENTA].descuento, 0)/[dbo].[ITEM_VENTA].cantidad)))*[dbo].[ITEM_VENTA].cantidad AS final, 1 as totalfinal "
                                "FROM [dbo].[ESTADO_PEDIDO] "
                                "JOIN [dbo].[VENTA] "
                                "ON [dbo].[VENTA].id_venta = [dbo].[ESTADO_PEDIDO].id_venta "
                                "JOIN [dbo].[ITEM_VENTA] "
                                "ON [dbo].[VENTA].id_venta = [dbo].[ITEM_VENTA].id_venta "
                                "JOIN [dbo].[PRODUCTO] "
                                "ON [dbo].[PRODUCTO].id_producto = [dbo].[ITEM_VENTA].id_producto "
                                "JOIN [dbo].[USUARIO] "
                                "ON [dbo].[USUARIO].id_usuario = [dbo].[VENTA].id_cliente "
                                "WHERE [dbo].[ESTADO_PEDIDO].estado = 'Carrito' "
                                f"AND [dbo].[USUARIO].id_usuario = {id_user} "
                                "EXCEPT (SELECT [dbo].[PRODUCTO].id_producto, [dbo].[PRODUCTO].foto, [dbo].[PRODUCTO].nombre, [dbo].[PRODUCTO].descripcion, [dbo].[PRODUCTO].precio, [dbo].[PRODUCTO].stock, ISNULL([dbo].[VENTA].total, 0) AS total, ISNULL([dbo].[VENTA].descuento, 0) * -1 AS descuento, [dbo].[ITEM_VENTA].cantidad AS cantidad,(ISNULL([dbo].[PRODUCTO].precio,0)-((ISNULL([dbo].[VENTA].descuento, 0)/[dbo].[ITEM_VENTA].cantidad)))*[dbo].[ITEM_VENTA].cantidad AS final, 1 as totalfinal "
                                "FROM [dbo].[ESTADO_PEDIDO] "
                                "JOIN [dbo].[VENTA] "
                                "ON [dbo].[VENTA].id_venta = [dbo].[ESTADO_PEDIDO].id_venta "
                                "JOIN [dbo].[ITEM_VENTA] "
                                "ON [dbo].[VENTA].id_venta = [dbo].[ITEM_VENTA].id_venta "
                                "JOIN [dbo].[PRODUCTO] "
                                "ON [dbo].[PRODUCTO].id_producto = [dbo].[ITEM_VENTA].id_producto "
                                "JOIN [dbo].[USUARIO] "
                                "ON [dbo].[USUARIO].id_usuario = [dbo].[VENTA].id_cliente "
                                "WHERE [dbo].[ESTADO_PEDIDO].estado = 'Pagado' "
                                f"AND [dbo].[USUARIO].id_usuario = {id_user}) ").fetchall()
    if len(result) == 0:
        return redirect('/catalogo/')
    for producto in result:
        producto.totalfinal = convertir(local,producto.total+producto.descuento)
        producto.total = convertir(local,producto.total)
        producto.descuento = convertir(local,producto.descuento)
        producto.final = convertir(local,producto.final)
        producto.precio = convertir(local,producto.precio)
    return render(request, 'ventasDatos.html', {'SQLVentDat':result})

def pagar(request, **kwargs):
    response = transbank.webpay_plus.create(datetime.now(), datetime.now(), float(kwargs.get('total')), "localhost:8000/carrito/validar")
    return response.token

def validarPago(request, **kwargs):
    response = transbank.webpay_plus.transaction.commit(pagar(request, **kwargs))
    return response.status