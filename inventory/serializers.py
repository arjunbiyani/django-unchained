from rest_framework import serializers
from inventory.models import inventory

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = inventory
        fields = '__all__'
    class Insert:
        model = inventory
        fields = ["sku_code",
                  "price",
                  "stock",
                  "created_at",
                  "created_by",
                  "updated_at",
                  ]
