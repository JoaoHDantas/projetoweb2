from rest_framework import viewsets
from interaction.models import Interaction
from interaction.api.serializers import InteractionSerializer

class InteractionViewSet(viewsets.ModelViewSet):
    queryset = Interaction.objects.all()
    serializer_class = InteractionSerializer