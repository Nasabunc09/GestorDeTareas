from django.contrib.auth.models import User
from django.db import models


class Tarea (models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True,null=True)
    
    estado = models.CharField(
        max_length = 20,
        choices = [ 
            ("pendiente","Pendiente"),
            ("progreso","En Progreso"),
            ("completada","Completada")
        ],
        default = "pendiente"
    )

    prioridad = models.CharField(
        max_length = 10,
        choices = [
            ("baja","Baja"),
            ("media","Media"),
            ("alta","Alta"),
        ],
        default = "media"
    )

    usuarios = models.ManyToManyField(User,related_name = "tareas")

    def __str__(self):
        return self.titulo

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rol = models.CharField(
        max_length=20,
        choices=[("admin", "Administrador"), ("estandar", "Usuario estándar")],
        default="estandar"
    )

    def __str__(self):
        return f"{self.user.username} ({self.rol})"

