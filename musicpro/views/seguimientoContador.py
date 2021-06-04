from .conn import *

def seguimientoContador(request):
    result = Conectar().execute("SELECT * FROM SEG_CONTADOR ORDER BY id_seg_cont ASC").fetchall()
    return render(request, 'seguimientoContador.html', {'SQLSegCont':result})