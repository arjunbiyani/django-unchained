from rest_framework import viewsets
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from inventory.serializers import InventorySerializer
from inventory.models import inventory

class InventoryView(viewsets.ModelViewSet):
    def get(self):
        queryset = inventory.objects.all().order_by('id')
        serializer_class = InventorySerializer(queryset, many=true)
        return HttpResponse(serializer_class.data)
    def post(self):
        pass




