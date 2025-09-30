from rest_framework import serializers
from .models import Tarea
from django.contrib.auth.models import User

# Serializador de Usuarios 
class UsuarioSerializer(serializers.ModelSerializer):
    rol = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ["id", "username", "email", "is_staff", "is_superuser", "rol"]

    def get_rol(self, obj):
        if obj.is_superuser:
            return "Superadministrador"
        elif obj.is_staff:
            return "Administrador"
        return "Usuario estándar"


# Serializador de Tareas 
class TareaSerializer(serializers.ModelSerializer):
    usuarios = serializers.PrimaryKeyRelatedField(
        many=True, queryset=User.objects.all()
    )
    usuarios_detalle = UsuarioSerializer(source="usuarios", many=True, read_only=True)

    class Meta:
        model = Tarea
        fields = [
            "id",
            "titulo",
            "descripcion",
            "estado",
            "prioridad",
            "usuarios",          
            "usuarios_detalle"   
        ]
