from .conn import *

def seguimientoVendedor(request):
    result = Conectar().execute("SELECT * FROM SEG_VENDEDOR ORDER BY id_seg_vend ASC").fetchall()
    return render(request, 'seguimientoVendedor.html', {'SQLSegVend':result})