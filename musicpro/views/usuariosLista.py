from .conn import *
from django.contrib.auth.models import User

@csrf_exempt
def viewUsuario(request, **kwargs):
    result = Usuario.objects.all().filter(id_usuario=kwargs.get('id')).values()
    if request.method == 'POST':
        return JsonResponse(list(result), safe=False)
    return render(request, 'productosDetalle.html', {'SQLProducto':result})

def viewUsuariosLista(request):
    result = Usuario.objects.all().exclude(nombre__istartswith='anon')
    buscar = ""
    if 'buscar' in request.GET:
        buscar = request.GET['buscar']
        if buscar == '':
            return redirect('/usuariosLista/')
        result = result.filter(nombre__icontains=buscar)
    return render(request, 'usuariosLista.html', {'SQLUsuarios':result, 'filtro':buscar})

@csrf_exempt
def newUsuario(request):
    if request.method == "POST":
        usuario = Usuario.objects.create(mail=request.POST['txt_mail'],
                                             rut=request.POST['txt_rut'],
                                             dv_rut=request.POST['txt_dv'],
                                             nombre=request.POST['txt_nombre'],
                                             telefono=request.POST['txt_fono'],
                                             direccion=request.POST['txt_direccion'],
                                             rol=request.POST['cmb_rol'])
        usuario.save()
        user = User.objects.create_user(username=usuario.nombre,
                                        email=usuario.mail,
                                        password=request.POST['txt_rut'])
        if usuario.rol == "Admin":
            user.is_staff = True
        user.save()
    return redirect('/usuariosLista/')
    
@csrf_exempt
def editUsuario(request, **kwargs):
    id = kwargs.get('id')
    if request.method == "POST":
        result = Conectar().execute("SELECT * "
                                    "FROM [dbo].[USUARIO] "
                                    f"WHERE [dbo].[USUARIO].[id_usuario] = {id} ").fetchone()
        nomUsuario = result
        usuario = User.objects.get(username=nomUsuario.nombre)
        usuario.email = request.POST['txt_mail']
        if request.POST['cmb_rol'] == "Admin":
            usuario.is_staff = True
        else:
            usuario.is_staff = False
        usuario.save()
        insertarVenta = Conectar().execute("UPDATE [dbo].[USUARIO] "
                                            f"SET [mail] = '{request.POST['txt_mail']}' "
                                            f",[rut] = {request.POST['txt_rut']} "
                                            f",[dv_rut] = '{request.POST['txt_dv']}' "
                                            f",[nombre] = '{request.POST['txt_nombre']}' "
                                            f",[telefono] = {request.POST['txt_fono']} "
                                            f",[direccion] = '{request.POST['txt_direccion']}' "
                                            f",[rol] = '{request.POST['cmb_rol']}' "
                                            f"WHERE [dbo].[USUARIO].[id_usuario] = {id} ")
        conn.commit()
    return redirect('/usuariosLista/')
