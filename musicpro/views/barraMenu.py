from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import *
from django.shortcuts import redirect


def login(request):
    user = request.POST["usuario"]
    pwrd = request.POST["contraseña"]
    usuario = authenticate(request, username=user, password=pwrd)
    if usuario is not None:
        auth_login(request, usuario)
        return redirect("/catalogo/")
    else:
        return redirect("../../")

@csrf_exempt
@require_POST
def tryPass(request):
  user = request.POST["mail"]
  pwrd = request.POST["pass"]
  usuario = authenticate(request, username=user, password=pwrd)
  if usuario is not None:
    return HttpResponse("Ok")
  else:
    return HttpResponse("Usuario/Contraseña incorrectos")

@login_required
def logout(request):
    auth_logout(request)
    return redirect("../../")
