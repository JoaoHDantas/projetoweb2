from rest_framework import viewsets, permissions
from interaction.models import Interaction
from interaction.api.serializers import InteractionSerializer
from .permissions import IsInSpecificGroup

class InteractionViewSet(viewsets.ModelViewSet):
    queryset = Interaction.objects.all()
    serializer_class = InteractionSerializer
    permission_classes = [permissions.IsAuthenticated, IsInSpecificGroup, permissions.DjangoModelPermissions]
    def get_queryset(self):
        # Obter o parâmetro 'pixelPost' da URL, se estiver presente
        pixel_id = self.request.query_params.get('pixelPost', None)
        
        # Se 'pixelPost' estiver presente, filtrar as interações associadas a esse Pixel específico
        if pixel_id is not None:
            return Interaction.objects.filter(pixelPost_id=pixel_id)
        
        # Caso contrário, retornar todas as interações
        return Interaction.objects.all()