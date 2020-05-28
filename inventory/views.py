from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse , JsonResponse
from django.shortcuts import get_object_or_404
from inventory.serializers import InventorySerializer
from inventory.models import inventory

@api_view(['GET'])
def getInventory(request):
    inventories = inventory.objects.all().order_by('id')
    serializer_class = InventorySerializer(inventories, many=True)
    return Response(serializer_class.data)




