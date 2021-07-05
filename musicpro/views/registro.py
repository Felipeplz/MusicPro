from .conn import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


def registroView(request):
    return render(request, "registro.html")


@require_POST
def registrarse(request):
    if request.user.is_authenticated and not request.user.username.startswith("anon"):
        return redirect("catalogo/")
    username = request.POST.get("user")
    password = request.POST.get("pass")
    user = authenticate(request, username=username, password=password)
    if user is not None:
        return HttpResponse("El usuario ya existe")
    user = User.objects.create_user(
        username=username, email=username, password=password
    )
    usuario, created = Usuario.objects.get_or_create(
        mail=user.username, rut="1", rol="Cliente"
    )
    if not request.POST.get("suscrito") == None:
        usuario.suscrito = True
        usuario.save()
    login(request, user)
    return HttpResponse("Ok")
