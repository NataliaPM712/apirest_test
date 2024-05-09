from .models import Empleados
from rest_framework import serializers

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleados
        fields = ('id',  'identificacion', 'nombre', 'apellidos', 'correo', 'salario_base', 'activo')