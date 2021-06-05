from .conn import *

#from .forms import UsuarioForm
#from .models import SQLUsuarios


def viewUsuarios(request):
    result = Conectar().execute("SELECT id_usuario, mail, rut, dv_rut, nombre, direccion," 
     "rol FROM USUARIO ORDER BY USUARIO.id_usuario ASC").fetchall()
    return render(request, 'usuariosLista.html', {'SQLUsuarios':result})
