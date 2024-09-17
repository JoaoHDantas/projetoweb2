from rest_framework import permissions

class IsInSpecificGroup(permissions.BasePermission):
    pixelPoster = 'pixelPoster'
    def has_permission (self, request, view):
        return request.user.groups.filter(name=self.pixelPoster).exists()
    
# class CanViewPostsGroup(permissions.BasePermission):
#     pixelViewer = 'pixelViewer'
#     def has_permission(self,request, view):
#         return request.user.groups.filter(name=self.pixelViewer).exists()