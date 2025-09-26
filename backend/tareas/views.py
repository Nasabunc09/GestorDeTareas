from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Tarea
from .serializers import TareaSerializer
from .permissions import EsPropietarioAdmin

class TareaViewSet(viewsets.ModelViewSet):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer
    permission_classes = [IsAuthenticated, EsPropietarioAdmin]

    def get_queryset(self):
        usuario = self.request.user
        if usuario.is_staff or usuario.is_superuser:
            return Tarea.objects.all()
        return Tarea.objects.filter(usuarios=usuario)