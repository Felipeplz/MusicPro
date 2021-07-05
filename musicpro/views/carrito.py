from .conn import *
from .moneda import getLocale

def productosCarrito(request):
    local = getLocale(request)
    usuario = getUsuario(request.user.username)
    try:
        venta = Venta.objects.filter(cliente=usuario, estado__estado__in=['En Carrito']).exclude(estado__estado__in=['Pagado',"Pago Pendiente"]).get()
    except:
        return redirect('../../catalogo/')
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
    if total == 0:
        return redirect('../../catalogo/')
    return render(request, 'carrito.html', {'venta':venta, 'local':local, 'total':total, 'subtotal':subtotal, 'descuento':descuento, 'usuario':usuario})

def comprobarVentaCarrito(id_cliente):
    result = Venta.objects.filter(cliente=id_cliente, estado__estado__in=['En Carrito']).exclude(estado__estado__in=['Pagado',"Pago Pendiente"]).first()
    return result

def comprobarItemVentaCarrito(venta, producto):
    result = ItemVenta.objects.filter(venta=venta, producto=producto).first()
    return result

@csrf_exempt
@require_POST
def anniadirCarrito(request):
    venta = comprobarVentaCarrito(getUsuario(request.user.email).id)
    if not venta:
        usuario = Usuario.objects.get(mail=request.user.username)
        venta = Venta.objects.create(cliente=usuario)
        estado = Estado.objects.create(venta=venta,
                                        estado='En Carrito')
    if request.method == 'POST':
        cantidad = 1
        if 'cantidad' in request.POST:
            cantidad = int(request.POST['cantidad'])
        producto = Producto.objects.filter(id=request.POST['id']).first()
        itemventa = comprobarItemVentaCarrito(venta, producto)
        if not itemventa:
            itemventa = ItemVenta.objects.create(venta=venta,
                                                producto=producto,
                                                cantidad=cantidad)
        else:
            itemventa.cantidad = cantidad
            itemventa.save()
    return HttpResponse("ok")

@csrf_exempt
@require_POST
def quitarCarrito(request):
    venta = comprobarVentaCarrito(getUsuario(request.user.email).id)
    if venta:
        if request.method == 'POST':
            producto = Producto.objects.filter(id=request.POST['id']).first()
            itemventa = comprobarItemVentaCarrito(venta, producto)
            itemventa.delete()
    return HttpResponse("ok")

@csrf_exempt
@require_POST
def cambiarCarrito(request):
    venta = comprobarVentaCarrito(getUsuario(request.user.email).id)
    if venta:
        if request.method == 'POST':
            producto = Producto.objects.filter(id=request.POST['id']).first()
            itemventa = comprobarItemVentaCarrito(venta, producto)
            print(itemventa)
            itemventa.cantidad = request.POST['cantidad']
            itemventa.save()
    return HttpResponse("ok")

@csrf_exempt
@require_POST
def limpiarCarrito(request):
    venta = comprobarVentaCarrito(getUsuario(request.user.email).id)
    if venta:
        venta.delete()
    return HttpResponse("ok")