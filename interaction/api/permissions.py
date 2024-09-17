from rest_framework import permissions

class IsInSpecificGroup(permissions.BasePermission):
    comentarios = 'comentarios'
    def has_permission (self, request, view):
        return request.user.groups.filter(name=self.comentarios).exists()