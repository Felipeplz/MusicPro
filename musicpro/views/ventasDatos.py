from .conn import *
from datetime import datetime
from transbank.error.transbank_error import TransbankError
from transbank.webpay.webpay_plus.transaction import Transaction
from .moneda import getLocale, convertir
import random
id_user = 5

@csrf_exempt
def ventasDatos(request):
    if ('token_ws' in request.POST):
        token = request.POST['token_ws']
        response = Transaction.commit(token)
        if (response.status == "AUTHORIZED"):
            return HttpResponse("PAGO REALIZADO")
        elif (response.status == "FAILED"):
            return HttpResponse("PAGO FALLÓ :o")
    local = getLocale(request)
    result = Conectar().execute("SELECT [dbo].[PRODUCTO].id_producto, [dbo].[PRODUCTO].foto, [dbo].[PRODUCTO].nombre, [dbo].[PRODUCTO].descripcion, [dbo].[PRODUCTO].precio, [dbo].[PRODUCTO].stock, "
                                "ISNULL([dbo].[PRODUCTO].precio*[dbo].[ITEM_VENTA].cantidad, 0) AS total, "
                                "ROUND([dbo].[VENTA].total * ISNULL(MAX([dbo].[PROMOCION].descuento), 0), 0) AS descuento, "
                                "[dbo].[ITEM_VENTA].cantidad AS cantidad, "
                                "ROUND(ISNULL([dbo].[PRODUCTO].precio*[dbo].[ITEM_VENTA].cantidad, 0) * ISNULL(1-MAX([dbo].[PROMOCION].descuento), 1), 0) AS final "
                                "FROM [dbo].[ESTADO_PEDIDO] "
                                "JOIN [dbo].[VENTA] "
                                "ON ([dbo].[VENTA].id_venta = [dbo].[ESTADO_PEDIDO].id_venta "
                                f"AND [dbo].[VENTA].id_venta = (SELECT MAX([dbo].[VENTA].id_venta) FROM [dbo].[VENTA] WHERE [dbo].[VENTA].[id_cliente] = {id_user})) "
                                "JOIN [dbo].[ITEM_VENTA] "
                                "ON [dbo].[VENTA].id_venta = [dbo].[ITEM_VENTA].id_venta "
                                "JOIN [dbo].[PRODUCTO] "
                                "ON [dbo].[PRODUCTO].id_producto = [dbo].[ITEM_VENTA].id_producto "
                                "JOIN [dbo].[USUARIO] "
                                "ON [dbo].[USUARIO].id_usuario = [dbo].[VENTA].id_cliente "
                                "LEFT JOIN [dbo].[PROMOCION] "
                                "ON (([dbo].[PRODUCTO].id_producto = [dbo].[PROMOCION].id_producto "
                                "AND [dbo].[ITEM_VENTA].cantidad >= [dbo].[PROMOCION].cantidad_min) "
                                "OR ([dbo].[PROMOCION].id_producto IS NULL "
                                "AND [dbo].[ITEM_VENTA].cantidad >= [dbo].[PROMOCION].cantidad_min)) "
                                "WHERE [dbo].[ESTADO_PEDIDO].estado = 'Carrito' "
                                f"AND [dbo].[USUARIO].id_usuario = {id_user} "
                                "GROUP BY [dbo].[PRODUCTO].id_producto, [dbo].[PRODUCTO].foto, [dbo].[PRODUCTO].nombre, [dbo].[PRODUCTO].descripcion, [dbo].[PRODUCTO].precio, [dbo].[PRODUCTO].stock, [dbo].[VENTA].total, [dbo].[ITEM_VENTA].cantidad "
                                "EXCEPT(SELECT [dbo].[PRODUCTO].id_producto, [dbo].[PRODUCTO].foto, [dbo].[PRODUCTO].nombre, [dbo].[PRODUCTO].descripcion, [dbo].[PRODUCTO].precio, [dbo].[PRODUCTO].stock, "
                                "ISNULL([dbo].[PRODUCTO].precio*[dbo].[ITEM_VENTA].cantidad, 0) AS total, "
                                "ROUND([dbo].[VENTA].total * ISNULL(MAX([dbo].[PROMOCION].descuento), 0), 0) AS descuento, "
                                "[dbo].[ITEM_VENTA].cantidad AS cantidad, "
                                "ROUND(ISNULL([dbo].[PRODUCTO].precio*[dbo].[ITEM_VENTA].cantidad, 0) * ISNULL(1-MAX([dbo].[PROMOCION].descuento), 0), 0) AS final "
                                "FROM [dbo].[ESTADO_PEDIDO] "
                                "JOIN [dbo].[VENTA] "
                                "ON [dbo].[VENTA].id_venta = [dbo].[ESTADO_PEDIDO].id_venta "
                                "JOIN [dbo].[ITEM_VENTA] "
                                "ON ([dbo].[VENTA].id_venta = [dbo].[ITEM_VENTA].id_venta "
                                f"AND [dbo].[VENTA].id_venta = (SELECT MAX([dbo].[VENTA].id_venta) FROM [dbo].[VENTA] WHERE [dbo].[VENTA].[id_cliente] = {id_user})) "
                                "JOIN [dbo].[PRODUCTO] "
                                "ON [dbo].[PRODUCTO].id_producto = [dbo].[ITEM_VENTA].id_producto "
                                "JOIN [dbo].[USUARIO] "
                                "ON [dbo].[USUARIO].id_usuario = [dbo].[VENTA].id_cliente "
                                "LEFT JOIN [dbo].[PROMOCION] "
                                "ON (([dbo].[PRODUCTO].id_producto = [dbo].[PROMOCION].id_producto "
                                "AND [dbo].[ITEM_VENTA].cantidad >= [dbo].[PROMOCION].cantidad_min) "
                                "OR ([dbo].[PROMOCION].id_producto IS NULL "
                                "AND [dbo].[ITEM_VENTA].cantidad >= [dbo].[PROMOCION].cantidad_min)) "
                                "WHERE [dbo].[ESTADO_PEDIDO].estado = 'Pagado' "
                                f"AND [dbo].[USUARIO].id_usuario = {id_user} "
                                "GROUP BY [dbo].[PRODUCTO].id_producto, [dbo].[PRODUCTO].foto, [dbo].[PRODUCTO].nombre, [dbo].[PRODUCTO].descripcion, [dbo].[PRODUCTO].precio, [dbo].[PRODUCTO].stock, [dbo].[VENTA].total, [dbo].[ITEM_VENTA].cantidad) ").fetchall()
    if len(result) == 0:
        return redirect('/catalogo/')
    totales = 0
    descuentos = 0
    subtotal = 0
    for producto in result:
        totales += producto.total
        descuentos += producto.descuento
        subtotal += producto.final
    #     producto.totalfinal = convertir(local,producto.total+producto.descuento)
    #     producto.total = convertir(local,producto.total)
    #     producto.descuento = convertir(local,producto.descuento)
    #     producto.final = convertir(local,producto.final)
    #     producto.precio = convertir(local,producto.precio)
    response = Transaction.create(str(random.randrange(1000000, 99999999)),str(random.randrange(1000000, 99999999)), subtotal, request.build_absolute_uri())
    totales = convertir(local,totales)
    descuentos = convertir(local,descuentos)
    if (local != "CLP"):
        total = str(convertir(local,subtotal)) + f" {local} -> " + str(subtotal) + " CLP"
    else:
        total = str(convertir(local,subtotal)) + f" {local}"
    subtotal = convertir(local,subtotal)
    return render(request, 'ventasDatos.html', {'SQLVentDat':result, 'local':local, 'response':response, 'totales': totales, 'descuentos': descuentos, 'subtotal': subtotal, 'total':total})

# def validarPago(request, **kwargs):
#     response = transbank.webpay.webpay_plus.transaction.commit(pagar(request, **kwargs))
#     return response.status