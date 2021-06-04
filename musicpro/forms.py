from django import forms
from .models import SQLUsuarios,SQLRoles

# class UsuarioForm(forms.UsuarioForm):
#     class Meta:
#         model = SQLUsuarios
#         fields=["id_usuario","dv_rut","nombre","telefono","direccion","mail","id_rol"]
class UsuarioForm(forms.Form):

    nombre= forms.CharField(max_length=100)
    


 