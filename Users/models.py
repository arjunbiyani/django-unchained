from django.db import models

# Create your models here.

class Users(models.Model):
    id = models.IntegerField
    name=models.CharField(max_length=60)
    username = models.CharField(max_length=60)
    created_at = models.DateTimeField('date published')
    updated_at = models.DateTimeField('date updated')

    def __str__(self):
        return self.id

class settings(models.Model):
    id = models.IntegerField
    user_id= models.IntegerField
    created_at = models.DateTimeField('date published')
    updated_at = models.DateTimeField('date updated')

    def __str__(self):
        return self.id