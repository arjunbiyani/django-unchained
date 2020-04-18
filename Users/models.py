from django.db import models

# Create your models here.

class Users(models.Model):
    id = models.IntegerField
    username = models.CharField(max_length=60)
    created_at = models.DateTimeField('date published')

    def __str__(self):
        return self.id

class settings(models.Model):
    id = models.IntegerField
    user_id= models.IntegerField
    created_at = models.DateTimeField('date published')

    def __str__(self):
        return self.id