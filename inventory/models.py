from django.db import models


# Create your models here.
class inventory(models.Model):
    id = models.IntegerField
    sku_code = models.CharField(max_length=60)
    created_at = models.DateTimeField('date published')
    updated_at = models.DateTimeField('date published')

    def __str__(self):
        return self.id