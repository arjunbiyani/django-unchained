from django.db import models
from viewflow.models import Process
# Create your models here.

class fnolProcess(Process):
    text = models.CharField(max_length=150)
    approved = models.BooleanField(default=False)

