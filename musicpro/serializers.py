from .models import SQLProductos, SQLUsuarios
from rest_framework import serializers

class ProductoSerializer(serializers.ModelSerializer):
    id_producto = serializers.ReadOnlyField()

    class Meta:
        model = SQLProductos
        fields = '__all__'
        
class UsuarioSerializer(serializers.ModelSerializer):
    id_usuario = serializers.ReadOnlyField()

    class Meta:
        model = SQLUsuarios
        exclude = ['contrasennia']