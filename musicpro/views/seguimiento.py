from django.db.models.expressions import Value
from .conn import *
from .moneda import getLocale
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

def seguimientoView(request):
    local = getLocale(request)
    usuario = getUsuario(request.user.username)
    ventas = Venta.objects.filter(estado__estado__in=['Pago Pendiente','Pagado','En Camino','Enviado','Entregado'])
    if usuario.rol == "Cliente":
      ventas = ventas.filter(cliente=usuario)
      return render(request, "seguimientoCliente.html", {"ventas": ventas, "local":local})
    elif usuario.rol == "Vendedor":
      ventas = ventas.filter(estado__estado__in=['Pagado'])
    elif usuario.rol == "Bodeguero":
      misventas = ventas.filter(estado__estado__in=['Pagado','En Camino','Enviado'], estado__encargado=usuario)
      ventas = ventas.filter(estado__estado__in=['Pagado','En Camino','Enviado'], estado__encargado=None)
      return render(request, "seguimientoBodeguero.html", {"ventas": ventas, "misventas": misventas, "local":local})
    elif usuario.rol == "Contador":
      ventas = ventas.filter(estado__estado__in=['Pago Pendiente','Enviado'])
    return render(request, "reporteriaVentas.html", {"ventas": ventas, "local":local})

@csrf_exempt
@require_POST
@login_required
def cargarVenta(request, **kwargs):
    id = kwargs.get("id")
    usuario = getUsuario(request.user.username)
    venta = Venta.objects.get(id=id)
    if usuario.rol == "Admin":
      usuario = venta.cliente
    items = ItemVenta.objects.filter(venta=venta).annotate(promo=Value(usuario.suscrito))
    return JsonResponse(list(items.values('producto__nombre','producto__precio','cantidad','promo')), safe=False)

@csrf_exempt
@require_POST
@login_required
def tomarVenta(request, **kwargs):
    id = kwargs.get("id")
    usuario = getUsuario(request.user.username)
    venta = Venta.objects.get(id=id)
    if usuario.rol == "Bodeguero":
      estadoId = venta.estado_set.last().id
      estado = Estado.objects.get(id=estadoId)
      estado.encargado = usuario
      estado.save()
    return HttpResponse("Ok")