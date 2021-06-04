from .conn import *

def ventaDatos(request):
    result = Conectar().execute("SELECT * FROM VENTA_DATOS ORDER BY id_vent_dat ASC").fetchall()
    return render(request, 'ventasDatos.html', {'SQLVentDat':result})