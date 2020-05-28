from django.urls import  path, include
from . import views
from rest_framework import  routers
router= routers.DefaultRouter()
urlpatterns=[
    path('all',
         views.getInventory,
         name='inventory'),
    path('add',
         views.insertInventory,
         name='Inser inventory')
]

