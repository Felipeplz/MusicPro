from .conn import *

@csrf_exempt
def viewProducto(request, **kwargs):
    id = kwargs.get('id')
    result = Conectar().execute("SELECT [id_producto] "
                                ",[codigo_producto] "
                                ",[nombre] "
                                ",[foto] "
                                ",[marca] "
                                ",[precio] "
                                ",[tipo] "
                                ",[subtipo] "
                                ",[categoria] "
                                ",[stock] "
                                ",[descripcion] "
                                "FROM [dbo].[PRODUCTO] "
                                f"WHERE [id_producto] = {id} ").fetchone()
    if request.method == 'POST':
        return JsonResponse(list(result), safe=False)
    return render(request, 'productosDetalle.html', {'SQLProducto':result})
