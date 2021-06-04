from .conn import *

def viewUsuarios(request):
    result = Conectar().execute("SELECT USUARIO.id_usuario, USUARIO.mail, USUARIO.rut, USUARIO.dv_rut, USUARIO.nombre, USUARIO.direccion," 
     "ROL.nombre_rol FROM USUARIO INNER JOIN ROL ON USUARIO.id_rol = ROL.id_rol ORDER BY USUARIO.id_usuario ASC").fetchall()
    return render(request, 'usuariosLista.html', {'SQLUsuarios':result})