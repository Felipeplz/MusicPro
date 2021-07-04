from .conn import *
from datetime import datetime
from transbank.error.transbank_error import TransbankError
from transbank.webpay.webpay_plus.transaction import Transaction
from .moneda import getLocale, convertir
import random


@csrf_exempt
def ventasDatos(request):
    local = getLocale(request)
    usuario = getUsuario(request.user.username)
    venta = (
        Venta.objects.filter(cliente=usuario, estado__estado__in=["En Carrito"])
        .exclude(estado__estado__in=["Pagado"])
        .get()
    )
    if venta == None:
        return redirect("../../catalogo/")
    total = 0
    subtotal = 0
    descuento = 0
    for item in venta.itemventa_set.all():
        total += item.producto.precio * item.cantidad
        subtotal += item.producto.precio * item.cantidad
        if item.cantidad >= 4:
            descuento += item.producto.precioPromo * item.cantidad
        else:
            descuento += item.producto.precio * item.cantidad
    if usuario.suscrito:
        response = Transaction.create(
            str(random.randrange(1000000, 99999999)),
            str(random.randrange(1000000, 99999999)),
            descuento,
            "http://" + request.get_host() + "/transbank/?usuario=" + usuario.nombre,
        )
    else:
        response = Transaction.create(
            str(random.randrange(1000000, 99999999)),
            str(random.randrange(1000000, 99999999)),
            total,
            "http://" + request.get_host() + "/transbank/?usuario=" + usuario.nombre,
        )
    sucursales = Sucursal.objects.all()
    return render(
        request,
        "ventasDatos.html",
        {
            "venta": venta,
            "local": local,
            "response": response,
            "total": total,
            "descuento": descuento,
            "subtotal": subtotal,
            "usuario": usuario,
            "sucursales": sucursales,
        },
    )
