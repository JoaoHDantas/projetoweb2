from rest_framework import permissions

class IsInSpecificGroup(permissions.DjangoModelPermissions):
    userProfileGen = 'userProfileGen'
    def has_permission (self, request, view):
        return request.user.groups.filter(name=self.userProfileGen).exists()