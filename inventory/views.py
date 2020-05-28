from rest_framework.response import Response
from rest_framework.decorators import api_view
from inventory.serializers import InventorySerializer
from inventory.models import inventory

@api_view(['GET'])
def getInventory(self):
    inventories = inventory.objects.all().order_by('id')
    serializer = InventorySerializer(inventories, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def insertInventory(request):
    serializer = InventorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)




