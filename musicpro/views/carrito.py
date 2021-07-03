from .conn import *
from .moneda import getLocale, convertir

def productosCarrito(request):
    local = getLocale(request)
    result = Venta.objects.all
    result = Conectar().execute("SELECT [dbo].[PRODUCTO].id_producto, [dbo].[PRODUCTO].foto, [dbo].[PRODUCTO].nombre, [dbo].[PRODUCTO].descripcion, [dbo].[PRODUCTO].precio, [dbo].[PRODUCTO].stock, "
                                "ISNULL([dbo].[PRODUCTO].precio*[dbo].[ITEM_VENTA].cantidad, 0) AS total, "
                                "ROUND([dbo].[VENTA].total * ISNULL(MAX([dbo].[PROMOCION].descuento), 0), 0) AS descuento, "
                                "[dbo].[ITEM_VENTA].cantidad AS cantidad, "
                                "ROUND(ISNULL([dbo].[PRODUCTO].precio*[dbo].[ITEM_VENTA].cantidad, 0) * ISNULL(1-MAX([dbo].[PROMOCION].descuento), 1), 0) AS final "
                                "FROM [dbo].[ESTADO_PEDIDO] "
                                "JOIN [dbo].[VENTA] "
                                "ON ([dbo].[VENTA].id_venta = [dbo].[ESTADO_PEDIDO].id_venta "
                                f"AND [dbo].[VENTA].id_venta = (SELECT MAX([dbo].[VENTA].id_venta) FROM [dbo].[VENTA] WHERE [dbo].[VENTA].[id_cliente] = {request.user.id})) "
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
                                "WHERE [dbo].[VENTA].token IS NULL "
                                f"AND [dbo].[USUARIO].id_usuario = {request.user.id} "
                                "GROUP BY [dbo].[PRODUCTO].id_producto, [dbo].[PRODUCTO].foto, [dbo].[PRODUCTO].nombre, [dbo].[PRODUCTO].descripcion, [dbo].[PRODUCTO].precio, [dbo].[PRODUCTO].stock, [dbo].[VENTA].total, [dbo].[ITEM_VENTA].cantidad ").fetchall()
    if len(result) == 0:
        return redirect('/catalogo/')
    totales = 0
    descuentos = 0
    subtotal = 0
    for producto in result:
        totales += producto.total
        descuentos += producto.descuento
        subtotal += producto.final
        producto.precio = convertir(local,producto.precio)
        producto.total = convertir(local,producto.total)
        producto.descuento = convertir(local,producto.descuento)
        producto.final = convertir(local,producto.final)
    totales = convertir(local,totales)
    descuentos = convertir(local,descuentos)
    subtotal = convertir(local,subtotal)
    return render(request, 'carrito.html', {'SQLCarrito':result, 'local':local, 'totales': totales, 'descuentos': descuentos, 'subtotal': subtotal})

def comprobarVentaCarrito(id_cliente):
    result = Conectar().execute("SELECT [dbo].[VENTA].[id_venta] "
                                "FROM [dbo].[VENTA] "
                                f"WHERE [dbo].[VENTA].[id_cliente] = {id_cliente} "
                                "AND [dbo].[VENTA].[token] IS NULL ").fetchone()
    return result

def comprobarItemVentaCarrito(id_venta, id_producto):
    result = Conectar().execute("SELECT [dbo].[ITEM_VENTA].[id_venta] "
                                "FROM [dbo].[ITEM_VENTA] "
                                f"WHERE [dbo].[ITEM_VENTA].[id_venta] = {id_venta} "
                                f"AND [dbo].[ITEM_VENTA].[id_producto] = {id_producto} ").fetchone()
    return result

@csrf_exempt
def anniadirCarrito(request):
    id_venta = comprobarVentaCarrito(request.user.id)
    if not id_venta:
        insertarVenta = Conectar().execute("INSERT INTO [dbo].[VENTA] "
                                           "([fecha] "
                                           ",[id_cliente]) "
                                           "VALUES "
                                           "(GETDATE() "
                                           f",{request.user.id})")
        conn.commit()
        id_venta = comprobarVentaCarrito(request.user.id)
        insertarEstado = Conectar().execute("INSERT INTO [dbo].[ESTADO_PEDIDO] "
                                            "([id_venta] "
                                            ",[fecha_estado] "
                                            ",[estado]) "
                                            "VALUES "
                                            f"({id_venta[0]} "
                                            ",GETDATE() "
                                            ",'Carrito')")
        conn.commit()
    if request.method == 'POST':
        cantidad = 1
        if 'cantidad' in request.POST:
            cantidad = int(request.POST['cantidad'])
            print(id_venta[0])
            print(request.POST['id'])
            print(cantidad)
        result = Conectar().execute("BEGIN "
                                        "IF NOT EXISTS (SELECT * "
                                        "FROM [dbo].[ITEM_VENTA] "
                                        f"WHERE [id_venta] = {id_venta[0]} "
                                        f"AND [id_producto] = {request.POST['id']}) "
                                        "BEGIN "
                                            "INSERT INTO [dbo].[ITEM_VENTA] "
                                            "([id_venta] "
                                            ",[id_producto] "
                                            ",[cantidad]) "
                                            "VALUES "
                                            f"({id_venta[0]} "
                                            f",{request.POST['id']} "
                                            f",{cantidad}) "
                                        "END "
                                        "ELSE "
                                        "BEGIN "
                                            "UPDATE [dbo].[ITEM_VENTA] "
                                            f"SET [cantidad] = {cantidad} "
                                            f"WHERE [id_venta] = {id_venta[0]} "
                                            f"AND [id_producto] = {request.POST['id']} "
                                        "END "
                                    "END ")
        conn.commit()
    return HttpResponse("ok")

@csrf_exempt
def quitarCarrito(request):
    id_venta = comprobarVentaCarrito(request.user.id)
    if id_venta[0]:
        if request.method == 'POST':
            result = Conectar().execute("DELETE FROM [dbo].[ITEM_VENTA] "
                                        f"WHERE [id_venta] = {id_venta[0]} "
                                        f"AND [id_producto] = {request.POST['id']}")
            conn.commit()
    return HttpResponse("ok")

@csrf_exempt
def cambiarCarrito(request):
    id_venta = comprobarVentaCarrito(request.user.id)
    if id_venta[0]:
        if request.method == 'POST':
            result = Conectar().execute("UPDATE [dbo].[ITEM_VENTA] "
                                        f"SET [cantidad] = {request.POST['cantidad']} "
                                        f"WHERE [id_venta] = {id_venta[0]} "
                                        f"AND [id_producto] = {request.POST['id']}")
            conn.commit()
    return HttpResponse("ok")