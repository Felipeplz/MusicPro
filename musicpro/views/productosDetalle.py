from .conn import *
from .moneda import getLocale


@csrf_exempt
def viewProducto(request, **kwargs):
    id = kwargs.get("id")
    local = getLocale(request)
    result = Producto.objects.get(id=id)
    if request.method == "POST":
        return JsonResponse(list(result.values()), safe=False)
    return render(
        request, "productosDetalle.html", {"producto": result, "local": local}
    )
