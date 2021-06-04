from .conn import *

def VentasConfirmar(request):
    result = Conectar().execute("SELECT * FROM VENT_CONFIRMAR ORDER BY id_vent_confir ASC").fetchall()
    return render(request, 'ventasConfirmar.html', {'SQLVentConfir':result})