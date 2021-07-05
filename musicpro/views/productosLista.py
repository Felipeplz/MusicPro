from .conn import *
from .moneda import getLocale, convertir
from urllib.request import urlopen
from urllib.parse import quote
import json


def viewProductosLista(request):
    local = getLocale(request)
    productos = Producto.objects.all()
    if "buscar" in request.GET:
      productos = productos.filter(nombre__icontains=request.GET.get("buscar"),
                                  descripcion__icontains=request.GET.get("buscar"))
    return render(
        request, "productosLista.html", {"productos": productos, "local": local}
    )

def safe_str(obj):
    try: return str(obj)
    except UnicodeEncodeError:
        return obj.encode('ascii', 'ignore').decode('ascii')
    return ""

safe_str(u'\u2013')

@csrf_exempt
def newProducto(request):
    if request.method == "POST" and "fil_foto" in request.FILES:
        fs = FileSystemStorage()
        archivo = request.FILES["fil_foto"]
        narchivo = fs.save(archivo.name, archivo)
        producto = Producto.objects.create(
            nombre=request.POST.get("txt_nombre"),
            foto=archivo.name,
            marca=request.POST.get("txt_marca"),
            precio=request.POST.get("txt_precio"),
            tipo=request.POST.get("txt_tipo"),
            subtipo=request.POST.get("txt_subtipo"),
            categoria=request.POST.get("cmb_categoria"),
            stock=request.POST.get("txt_stock"),
            descripcion=request.POST.get("txa_descripcion"),
        )
    return redirect("/productosLista/")


@csrf_exempt
def editProducto(request, **kwargs):
    id = kwargs.get("id")
    producto = Producto.objects.get(id=id)
    if request.method == "POST":
        query = ""
        if "fil_foto" in request.FILES:
            fs = FileSystemStorage()
            archivo = request.FILES["fil_foto"]
            narchivo = fs.save(archivo.name, archivo)
            query = f",[foto] = '{archivo.name}' "
            producto.foto = archivo.name
        producto.nombre = request.POST['txt_nombre']
        producto.marca = request.POST['txt_marca']
        producto.precio = request.POST['txt_precio']
        producto.tipo = request.POST['txt_tipo']
        producto.subtipo = request.POST['txt_subtipo']
        producto.categoria = request.POST['cmb_categoria']
        producto.stock = request.POST['txt_stock']
        producto.descripcion = request.POST['txa_descripcion']
        producto.save()
    return redirect("/productosLista/")
