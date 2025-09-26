from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Tarea

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","username"]

class TareaSerializer(serializers.ModelSerializer):
    usuarios = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Tarea
        fields = '__all__'