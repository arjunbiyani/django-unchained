from rest_framework import viewsets

from inventory.serializers import InventorySerializer
from inventory.models import inventory

class InventoryView(viewsets.ModelViewSet):
    queryset = inventory.objects.all().order_by('id')
    serializer_class = InventorySerializer


