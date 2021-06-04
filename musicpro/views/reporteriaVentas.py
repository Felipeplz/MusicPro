from .conn import *

def viewVentas(request, **kwargs):
    id = kwargs.get("id")
    result = Conectar().execute(f"SELECT *"
                            "FROM [dbo].[VENTA]"
                            "ORDER BY id_venta ASC").fetchall()
    return render(request, 'reporteriaVentas.html', {'SQLPromo':result})