from .conn import *
from django.views.decorators.csrf import csrf_exempt

#id_user = getCookie(request, "user")
id_user = 5

def productosCarrito(request):
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
    return render(request, 'carrito.html', {'SQLCarrito':result, 'local':local})

def comprobarVentaCarrito(id):
    result = Conectar().execute("SELECT [dbo].[VENTA].[id_venta] "
                                "FROM [dbo].[VENTA] "
                                "JOIN [dbo].[ESTADO_PEDIDO] "
                                "ON [dbo].[VENTA].[id_venta] = [dbo].[ESTADO_PEDIDO].[id_venta] "
                                f"WHERE [dbo].[VENTA].[id_cliente] = {id} "
                                "AND [dbo].[ESTADO_PEDIDO].[estado] = 'Carrito' "
                                "EXCEPT (SELECT [dbo].[VENTA].[id_venta] "
                                "FROM [dbo].[VENTA] "
                                "JOIN [dbo].[ESTADO_PEDIDO] "
                                "ON [dbo].[VENTA].[id_venta] = [dbo].[ESTADO_PEDIDO].[id_venta] "
                                f"WHERE [dbo].[VENTA].[id_cliente] = {id} "
                                "AND [dbo].[ESTADO_PEDIDO].[estado] = 'Pagado')").fetchone()
    return result

@csrf_exempt
def anniadirCarrito(request):
    id_venta = comprobarVentaCarrito(id_user)
    if not id_venta:
        insertarVenta = Conectar().execute("INSERT INTO [dbo].[VENTA] "
                                    "([fecha] "
                                    ",[id_cliente]) "
                                    "VALUES "
                                    "(GETDATE()"
                                    f",{id_user})")
        conn.commit()
        id_venta = Conectar().execute("SELECT [dbo].[VENTA].[id_venta] "
                                "FROM [dbo].[VENTA] "
                                f"WHERE [dbo].[VENTA].[id_cliente] = {id_user} "
                                "EXCEPT (SELECT [dbo].[VENTA].[id_venta] "
                                "FROM [dbo].[VENTA] "
                                "JOIN [dbo].[ESTADO_PEDIDO] "
                                "ON [dbo].[VENTA].[id_venta] = [dbo].[ESTADO_PEDIDO].[id_venta] "
                                f"WHERE [dbo].[VENTA].[id_cliente] = {id_user} "
                                "AND [dbo].[ESTADO_PEDIDO].[estado] = 'Pagado')").fetchone()
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
        result = Conectar().execute("INSERT INTO [dbo].[ITEM_VENTA] "
                                    "([id_venta] "
                                    ",[id_producto] "
                                    ",[cantidad]) "
                                    "VALUES "
                                    f"({id_venta[0]} "
                                    f",{request.POST['id']} "
                                    ",1)")
        conn.commit()
    return HttpResponse("ok")

@csrf_exempt
def quitarCarrito(request):
    id_venta = comprobarVentaCarrito(id_user)
    if id_venta[0]:
        if request.method == 'POST':
            result = Conectar().execute("DELETE FROM [dbo].[ITEM_VENTA] "
                                        f"WHERE [id_venta] = {id_venta[0]} "
                                        f"AND [id_producto] = {request.POST['id']}")
            conn.commit()
    return HttpResponse("ok")

@csrf_exempt
def cambiarCarrito(request):
    id_venta = comprobarVentaCarrito(id_user)
    if id_venta[0]:
        if request.method == 'POST':
            result = Conectar().execute("UPDATE [dbo].[ITEM_VENTA] "
                                        f"SET [cantidad] = {request.POST['cantidad']} "
                                        f"WHERE [id_venta] = {id_venta[0]} "
                                        f"AND [id_producto] = {request.POST['id']}")
            conn.commit()
    return HttpResponse("ok")