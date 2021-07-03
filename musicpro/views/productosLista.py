from .conn import *
from .moneda import getLocale, convertir
from urllib.request import urlopen
import json

def viewProductosLista(request):
    local = getLocale(request)
    if 'buscar' in request.GET:
        ws = urlopen('http://127.0.0.1:8000/api/producto?format=json&nombre=' + request.GET['buscar'])
    string = ws.read().decode('utf-8')
    result = json.loads(string)
    return render(request, 'productosLista.html', {'SQLProductos':result, 'local':local})

@csrf_exempt
def newProducto(request):
    if request.method == "POST" and "fil_foto" in request.FILES:
        fs = FileSystemStorage()
        archivo = request.FILES["fil_foto"]
        narchivo = fs.save(archivo.name, archivo)
        producto = Producto.objects.create(nombre=request.POST.get("txt_nombre"),
                                            foto=archivo.name,
                                            marca=request.POST.get("txt_marca"),
                                            precio=request.POST.get("txt_precio"),
                                            tipo=request.POST.get("txt_tipo"),
                                            subtipo=request.POST.get("txt_subtipo"),
                                            categoria=request.POST.get("cmb_categoria"),
                                            stock=request.POST.get("txt_stock"),
                                            descripcion=request.POST.get("txa_descripcion"))
    return redirect('/productosLista/')
    
@csrf_exempt
def editProducto(request, **kwargs):
    id = kwargs.get('id')
    if request.method == "POST":
        query = ""
        if "fil_foto" in request.FILES:
            fs = FileSystemStorage()
            archivo = request.FILES["fil_foto"]
            narchivo = fs.save(archivo.name, archivo)
            query = f",[foto] = '{archivo.name}' "
        insertarVenta = Conectar().execute("UPDATE [dbo].[PRODUCTO] "
                                            f"SET [codigo_producto] = '{request.POST['txt_nombre']}' "
                                            f",[nombre] = '{request.POST['txt_nombre']}' "
                                            + query + 
                                            f",[marca] = '{request.POST['txt_marca']}' "
                                            f",[precio] = {request.POST['txt_precio']} "
                                            f",[tipo] = '{request.POST['txt_tipo']}' "
                                            f",[subtipo] = '{request.POST['txt_subtipo']}' "
                                            f",[categoria] = '{request.POST['cmb_categoria']}' "
                                            f",[stock] = {request.POST['txt_stock']} "
                                            f",[descripcion] = '{request.POST['txa_descripcion']}' "
                                            f"WHERE [dbo].[PRODUCTO].[id_producto] = {id} ")
        conn.commit()
    return redirect('/productosLista/')