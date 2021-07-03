from musicpro.views.moneda import getIP
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import *
from django.shortcuts import redirect, render

def login(request):
    user = request.POST['usuario']
    pwrd = request.POST['contraseña']
    usuario = authenticate(request, username=user, password=pwrd)
    if usuario is not None:
        auth_login(request, usuario)
        return redirect('/catalogo/')
    else:
        request.session['respuesta'] = "La combinación de usuario y contraseña no es válida."
        return redirect('../../')

@login_required
def logout(request):
    auth_logout(request)
    return redirect('../../')