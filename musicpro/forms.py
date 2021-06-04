from django import forms
from .models import SQLUsuarios,SQLRoles

class CompradorForm(forms.ModelForm):
    class Meta:
        model = SQLUsuarios
        fields=["id_usuario","dv_rut","nombre","telefono","direccion","mail","nombre_rol"]




