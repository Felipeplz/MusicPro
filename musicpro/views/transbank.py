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
    if response.status == "AUTHORIZED":
      try:
        venta = Venta.objects.filter(cliente=usuario, estado__estado__in=['En Carrito']).exclude(estado__estado__in=['Pagado']).get()
        venta.token = token
        venta.total = response.amount
        venta.save()
        for item in venta.itemventa_set.all():
          item.producto.stock -= item.cantidad
          item.producto.save()
        estado = Estado.objects.create(venta=venta, estado='Pagado')
      except:
        pass
      return render(request, 'transbankCorrecto.html', {'respuesta':response, 'local':local})
    return render(request, 'transbankFallo.html', {'respuesta':response})