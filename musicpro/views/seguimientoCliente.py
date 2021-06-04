from .conn import *

def seguimientoCliente(request):
    result = Conectar().execute("SELECT * FROM SEG_CLIENTE ORDER BY id_seg_client ASC").fetchall()
    return render(request, 'seguimientoCliente.html', {'SQLSegClient':result})