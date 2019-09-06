from Customers.models import Customer
from rest_framework import viewsets,permissions
from .seriealizers import CustomerSerializer


#customer viewset 

class CustomerViewSet(viewsets.ModelViewSet):
    queryset =  Customer.objects.all()

    permission_classes=[
        permissions.AllowAny
    ]
    serializer_class= CustomerSerializer
    