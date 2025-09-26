from rest_framework import permissions

class EsPropietarioAdmin(permissions.BasePermission):

    def has_object_permission(self,request,view,obj):
        #Admin siempre tiene acceso
        if request.user.is_staff or request.user.is_superuser:
            return True
        
        #Usuario estandar solo si esta asignado a la tarea
        return request.user in obj.usuarios.all()