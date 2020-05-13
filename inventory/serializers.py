from rest_framework import serializers
from inventory.models import inventory

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = inventory
        fields = ['id','sku_code', 'sku_name', 'price', 'stocks','created_at']
