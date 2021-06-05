from .conn import *

def viewCatalogo(request, **kwargs):
    local = getLocale(request)

    if not (request.path.startswith("/catalogo/")):
        return redirect('/catalogo/')
    tab = kwargs.get('tab')
    if (tab == None):
        tab = "todos"
        query = ""
    else:
        if tab == "cuerda":
            query = "WHERE categoria = 'Instrumentos de Cuerdas'"
        elif tab == "percusion":
            query = "WHERE categoria = 'Percusión'"
        elif tab == "amplificadores":
            query = "WHERE categoria = 'Amplificadores'"
        elif tab == "accesorios":
            query = "WHERE categoria = 'Accesorios'"
    result = Conectar().execute("SELECT [dbo].[PRODUCTO].id_producto, "
                                "[dbo].[PRODUCTO].foto, "
                                "[dbo].[PRODUCTO].nombre, "
                                "[dbo].[PRODUCTO].descripcion, "
                                "[dbo].[PRODUCTO].precio, "
                                "[dbo].[PRODUCTO].stock, "
                                "[dbo].[PRODUCTO].precio - ([dbo].[PRODUCTO].precio * ISNULL([dbo].[PROMOCION].[descuento],0)) AS final "
                                "FROM [dbo].[PRODUCTO] "
                                "LEFT JOIN [dbo].[PROMOCION] "
                                "ON [dbo].[PROMOCION].[id_producto] = [dbo].[PRODUCTO].[id_producto] "
                                + query +
                                "ORDER BY [dbo].[PRODUCTO].[id_producto] ASC ").fetchall()
    for producto in result:
        producto.final = convertir(local,producto.final)
        producto.precio = convertir(local,producto.precio)
    return render(request, 'catalogo.html', {'SQLProductos':result, 'tab': tab, 'local':local})