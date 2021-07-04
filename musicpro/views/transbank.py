from .conn import *
from .moneda import getLocale, convertir
from transbank.webpay.webpay_plus.transaction import Transaction

@csrf_exempt
def transbankView(request):
    local = getLocale(request)
    if not "token_ws" in request.POST:
        return redirect('../../carrito/')
    token = request.POST['token_ws']
    usuario = getUsuario(request.GET.get("usuario"))
    response = Transaction.commit(token)
    if (response.status == "AUTHORIZED"):
        try:
            venta = Venta.objects.filter(idCliente=usuario, estado__estado__in=['En Carrito']).exclude(estado__estado__in=['Pagado']).get()
            venta.token = token
            venta.save()
            estado = Estado.objects.create(idVenta=venta,
                                    estado='Pagado')
        except:
            pass
        return render(request, 'transbankCorrecto.html', {'respuesta':response, 'local':local})
    elif (response.status == "FAILED"):
        return render(request, 'transbankFallo.html', {'respuesta':response})
    return render(request, 'transbankCorrecto.html',)