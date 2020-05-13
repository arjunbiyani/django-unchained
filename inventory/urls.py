from django.urls import  path, include
from . import views
from rest_framework import  routers

routers= routers.DefaultRouter()
routers.register('inventory',views.InventoryView)

urlpatterns=[
    path('inventory/',include(routers.urls))
]

