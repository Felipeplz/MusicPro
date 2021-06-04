from .conn import *

def productosCarrito(request):
    id_user = getCookie(request, "user")
    result = Conectar().execute("SELECT * "
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
                               f"AND [dbo].[VENTA].id_cliente = {id_user} ").fetchall()
    return render(request, 'carrito.html', {'SQLCarrito':result})