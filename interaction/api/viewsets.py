from rest_framework import viewsets, permissions
from interaction.models import Interaction
from interaction.api.serializers import InteractionSerializer
from .permissions import IsInSpecificGroup

class InteractionViewSet(viewsets.ModelViewSet):
    queryset = Interaction.objects.all()
    serializer_class = InteractionSerializer
    permission_classes = [permissions.IsAuthenticated, IsInSpecificGroup]