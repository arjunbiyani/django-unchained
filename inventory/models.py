from django.db import models


# Create your models here.
class inventory(models.Model):
    id = models.IntegerField(primary_key=True)
    sku_code = models.CharField(max_length=60)
    price = models.IntegerField
    stock = models.IntegerField
    created_at = models.DateTimeField('created at')
    updated_at = models.DateTimeField('updated at')

    def __str__(self):
        return self.id