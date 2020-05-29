from django.db import models


# Create your models here.
class inventory(models.Model):
    id = models.AutoField(primary_key=True)
    sku_code = models.CharField(max_length=60, unique=True)
    price = models.IntegerField()
    stock = models.IntegerField()
    created_by = models.CharField(max_length=60)
    created_at = models.DateTimeField('created at', auto_now_add=True)
    updated_at = models.DateTimeField('updated at', auto_now_add=True)

    def __int__(self):
        return self.id