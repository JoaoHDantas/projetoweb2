from rest_framework import routers
from interaction.api.viewsets import InteractionViewSet

interaction_router = routers.DefaultRouter()
interaction_router.register('interaction', InteractionViewSet)