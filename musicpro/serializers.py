from .models import Producto, Usuario
from rest_framework import serializers

class ProductoSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Producto
        fields = '__all__'
        
class UsuarioSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Usuario
        exclude = ['contrasennia']