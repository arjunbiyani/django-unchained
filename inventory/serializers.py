from rest_framework import serializers
from inventory.models import inventory

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = inventory
        fields = ['id',
                  'sku_code',
                  'price',
                  'stock',
                  'created_at',
                  'created_by',
                  'created_at'
                  ]

