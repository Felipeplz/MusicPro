from .models import SQLProductos
from rest_framework import serializers

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SQLProductos
        fields = '__all__'
        