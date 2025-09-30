from rest_framework import routers
from django.urls import path, include
from .views import TareaViewSet, UsuarioViewSet


# Creamos el router y registramos los ViewSets
router = routers.DefaultRouter()
router.register(r'tareas', TareaViewSet)
router.register(r'users', UsuarioViewSet)

urlpatterns = [
    path('', include(router.urls)),  # endpoints: /api/tareas/ y /api/users/
]