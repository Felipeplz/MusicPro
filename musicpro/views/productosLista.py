from .conn import *

def viewProductosLista(request):
    query = ""
    if 'buscar' in request.GET:
        if request.GET['buscar'] == '':
            return redirect('/productosLista/')
        query = f"WHERE [nombre] LIKE '%{request.GET['buscar']}%' "
    result = Conectar().execute("SELECT [dbo].[PRODUCTO].[id_producto]"
                                ",[codigo_producto]"
                                ",[nombre]"
                                ",[foto]"
                                ",[precio]"
                                ",[stock]"
                                ",[descripcion]"
                                ",CASE WHEN [descuento] IS NOT NULL THEN ROUND([precio] - ([precio] * ISNULL([descuento],0)), -1) ELSE [precio] END AS final "
                                "FROM [dbo].[PRODUCTO]"
                                "LEFT JOIN [dbo].[PROMOCION]"
                                "ON [dbo].[PROMOCION].[id_producto] = [dbo].[PRODUCTO].[id_producto] " + query).fetchall()
    return render(request, 'productosLista.html', {'SQLProductos':result})

@csrf_exempt
def newProducto(request):
    if request.method == "POST" and "fil_foto" in request.FILES:
        fs = FileSystemStorage()
        archivo = request.FILES["fil_foto"]
        narchivo = fs.save(archivo.name, archivo)
        insertarVenta = Conectar().execute("INSERT INTO [dbo].[PRODUCTO] "
                                            "([codigo_producto]"
                                            ",[nombre] "
                                            ",[foto] "
                                            ",[marca] "
                                            ",[precio] "
                                            ",[tipo] "
                                            ",[subtipo] "
                                            ",[categoria] "
                                            ",[stock] "
                                            ",[descripcion]) "
                                            "VALUES "
                                            f"('{request.POST['txt_nombre']}' "
                                            f",'{request.POST['txt_nombre']}' "
                                            f",'{archivo.name}' "
                                            f",'{request.POST['txt_marca']}' "
                                            f",{request.POST['txt_precio']} "
                                            f",'{request.POST['txt_tipo']}' "
                                            f",'{request.POST['txt_subtipo']}' "
                                            f",'{request.POST['cmb_categoria']}' "
                                            f",{request.POST['txt_stock']} "
                                            f",'{request.POST['txa_descripcion']}') ")
        conn.commit()
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