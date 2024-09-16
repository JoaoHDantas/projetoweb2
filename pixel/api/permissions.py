from rest_framework import permissions

class IsInSpecificGroup(permissions.DjangoModelPermissions):
    pixelPoster = 'pixelPoster'
    def has_permission (self, request, view):
        return request.user.groups.filter(name=self.pixelPoster).exists()
    
class CanViewPostsGroup(permissions.DjangoModelPermissions):
    pixelViewer = 'pixelViewer'
    def has_permission(self,request, view):
        return request.user.groups.filter(name=self.pixelViewer).exists()