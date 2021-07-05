from .conn import *
from django.contrib.auth.models import User


@csrf_exempt
def viewUsuario(request, **kwargs):
    result = Usuario.objects.all().filter(id=kwargs.get("id")).values()
    if request.method == "POST":
        return JsonResponse(list(result), safe=False)
    return render(request, "productosDetalle.html", {"SQLProducto": result})


def viewUsuariosLista(request):
    result = Usuario.objects.all().exclude(mail__istartswith="anon")
    buscar = ""
    if "buscar" in request.GET:
        buscar = request.GET["buscar"]
        if buscar == "":
            return redirect("/usuariosLista/")
        result = result.filter(mail__icontains=buscar)
    return render(request, "usuariosLista.html", {"usuarios": result, "filtro": buscar})


@csrf_exempt
def newUsuario(request):
    if request.method == "POST":
        usuario = Usuario.objects.create(
            mail=request.POST["txt_mail"],
            rut=request.POST["txt_rut"].replace(".", "").replace("-", ""),
            telefono=request.POST["txt_fono"],
            direccion=request.POST["txt_direccion"],
            rol=request.POST["cmb_rol"],
        )
        usuario.save()
        user = User.objects.create_user(
            username=usuario.mail, email=usuario.mail, password=request.POST["txt_rut"]
        )
        if usuario.rol == "Admin":
            user.is_staff = True
        user.save()
    return redirect("/usuariosLista/")


@csrf_exempt
def editUsuario(request, **kwargs):
    id = kwargs.get("id")
    usuarioU = Usuario.objects.get(id=id)
    if request.method == "POST":
        usuarioD = User.objects.get(username=usuarioU.mail)
        usuarioD.email = request.POST["txt_mail"]
        if request.POST["cmb_rol"] == "Admin":
            usuarioD.is_staff = True
        else:
            usuarioD.is_staff = False
        usuarioD.save()
        usuarioU.mail = request.POST["txt_mail"]
        usuarioU.rut = request.POST["txt_rut"].replace(".", "").replace("-", "")
        usuarioU.telefono = request.POST["txt_fono"]
        usuarioU.direccion = request.POST["txt_direccion"]
        usuarioU.rol = request.POST["cmb_rol"]
        usuarioU.save()
    return redirect("/usuariosLista/")
