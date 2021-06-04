from .conn import *

def viewCatalogo(request, **kwargs):
    if (request.path == "/"):
        return redirect('/catalogo')
    tab = kwargs.get('tab')
    if (tab == None):
        tab = "todos"
        query = ""
    else:
        query = f"WHERE categoria = '{tab}'"
    result = Conectar().execute("SELECT *"
                               f"FROM PRODUCTO {query}"
                                "ORDER BY id_producto ASC").fetchall()
    return render(request, 'catalogo.html', {'SQLProductos':result, 'tab': tab})