from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from .models import Tarea
from .serializers import TareaSerializer
from .serializers import UsuarioSerializer
from django.contrib.auth.models import User 

class TareaViewSet(viewsets.ModelViewSet):
    queryset = Tarea.objects.all()   # necesario para el router
    serializer_class = TareaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        usuario = self.request.user
        if usuario.is_staff or usuario.is_superuser:
            return Tarea.objects.all()
        return Tarea.objects.filter(usuarios=usuario)

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated] #solo los que estén logueados podrán ver usuarios