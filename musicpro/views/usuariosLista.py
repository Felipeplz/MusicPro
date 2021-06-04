from .conn import *
#from .forms import UsuarioForm
#from .models import SQLUsuarios


def viewUsuarios(request):
    result = Conectar().execute("SELECT USUARIO.id_usuario, USUARIO.mail, USUARIO.rut, USUARIO.dv_rut, USUARIO.nombre, USUARIO.direccion," 
     "ROL.nombre_rol FROM USUARIO INNER JOIN ROL ON USUARIO.id_rol = ROL.id_rol ORDER BY USUARIO.id_usuario ASC").fetchall()
    return render(request, 'usuariosLista.html', {'SQLUsuarios':result})

def RegistrarUsuario(request):
    form= UsuarioForm(request.POST or None)
    if form.is_valid():
        form_data= form.cleaned_data
        abc= form_data.get("nombre")
        obj= SQLUsuarios.objects.create(nombre=abc) 
    context ={
        "form": form,
     }
    return render(
        request,
        'usuarioslista.html', context)
    #data = {
          #'form': usuarioForm()   
  # }

# if request.method == 'POST':
#         formulario = UsuarioForm(data=request.POST)
#         if formulario.is_valid():
#              formulario.save()
#              data["mensaje"] = "Usuario Guardado"
#         else:
#             data["form"] = formulario
   
       