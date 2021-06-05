from .conn import *

@csrf_exempt
def viewUsuario(request, **kwargs):
    id = kwargs.get('id')
    result = Conectar().execute("SELECT [id_usuario]"
                                ",[mail]"
                                ",[contrasennia]"
                                ",[rut]"
                                ",[dv_rut]"
                                ",[nombre]"
                                ",[telefono]"
                                ",[direccion]"
                                ",[rol]"
                                "FROM [dbo].[USUARIO]"
                                f"WHERE [id_usuario] = {id} ").fetchone()
    if request.method == 'POST':
        return JsonResponse(list(result), safe=False)
    return render(request, 'productosDetalle.html', {'SQLProducto':result})

def viewUsuariosLista(request):
    query = ""
    if 'buscar' in request.GET:
        if request.GET['buscar'] == '':
            return redirect('/usuariosLista/')
        query = f"WHERE [nombre] LIKE '%{request.GET['buscar']}%' "
    result = Conectar().execute("SELECT [id_usuario]"
                                ",[mail]"
                                ",[contrasennia]"
                                ",[rut]"
                                ",[dv_rut]"
                                ",[nombre]"
                                ",[telefono]"
                                ",[direccion]"
                                ",[rol]"
                                "FROM [dbo].[USUARIO]" + query).fetchall()
    return render(request, 'usuariosLista.html', {'SQLUsuarios':result})

@csrf_exempt
def newUsuario(request):
    if request.method == "POST":
        insertarVenta = Conectar().execute("INSERT INTO [dbo].[USUARIO] "
                                            "([mail] "
                                            ",[rut] "
                                            ",[dv_rut] "
                                            ",[nombre] "
                                            ",[contrasennia] "
                                            ",[telefono] "
                                            ",[direccion] "
                                            ",[rol]) "
                                            "VALUES "
                                            f"('{request.POST['txt_mail']}' "
                                            f",{request.POST['txt_rut']} "
                                            f",'{request.POST['txt_dv']}' "
                                            f",'{request.POST['txt_nombre']}' "
                                            f",'{request.POST['txt_rut']}' "
                                            f",{request.POST['txt_fono']} "
                                            f",'{request.POST['txt_direccion']}' "
                                            f",'{request.POST['cmb_rol']}') ")
        conn.commit()
    return redirect('/usuariosLista/')
    
@csrf_exempt
def editUsuario(request, **kwargs):
    id = kwargs.get('id')
    if request.method == "POST":
        insertarVenta = Conectar().execute("UPDATE [dbo].[USUARIO] "
                                            f"SET [mail] = '{request.POST['txt_mail']}' "
                                            f",[rut] = {request.POST['txt_rut']} "
                                            f",[dv_rut] = '{request.POST['txt_dv']}' "
                                            f",[nombre] = '{request.POST['txt_nombre']}' "
                                            f",[contrasennia] = '{request.POST['txt_rut']}' "
                                            f",[telefono] = {request.POST['txt_fono']} "
                                            f",[direccion] = '{request.POST['txt_direccion']}' "
                                            f",[rol] = '{request.POST['cmb_rol']}' "
                                            f"WHERE [dbo].[USUARIO].[id_usuario] = {id} ")
        conn.commit()
    return redirect('/usuariosLista/')
