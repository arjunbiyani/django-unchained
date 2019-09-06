from django.db import models

# Create your models here.
class Customer(models.Model):
    name= models.CharField(max_length=100)
    email= models.EmailField(max_length=100,unique=True)
    username = models.CharField(max_length=50,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
