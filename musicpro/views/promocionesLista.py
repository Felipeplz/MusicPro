from .conn import *

def promociones(request):
    result = Conectar().execute("SELECT [dbo].[PRODUCTO].[id_producto]"
                                ",[codigo_producto]"
                                ",[nombre]"
                                ",[marca]"
                                ",[precio]"
                                ",[tipo]"
                                ",[subtipo]"
                                ",[categoria]"
                                ",[cantidad_min]"
                                ",[descuento]"
                            "FROM [dbo].[PRODUCTO] JOIN"
                            "[dbo].[PROMOCION] ON [dbo].[PRODUCTO].[id_producto] = [dbo].[PROMOCION].[id_producto]"
                            "WHERE GETDATE() BETWEEN [fecha_desde] AND [fecha_hasta]").fetchall()
    return render(request, 'promocionesLista.html', {'SQLPromo':result})