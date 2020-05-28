from django.urls import  path, include
from . import views
from rest_framework import  routers
from  django.conf.urls import url
router= routers.DefaultRouter()
urlpatterns=[
    path('all',
         views.getInventory,
         name='inventory'),
    path('add',
         views.insertInventory,
         name='Inser inventory')
]

