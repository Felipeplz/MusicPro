from .conn import *

def ventasDatos(request):
    result = Conectar().execute("SELECT direccion from venta v join usuario u on u.id_usuario = v.id_cliente join pago p on v.id_venta = p.id_venta;").fetchall()
    return render(request, 'ventasDatos.html', {'SQLVentDat':result})