from django.db import models
from django.db.models.fields import TextField
from django.db.models.deletion import CASCADE

# Create your models here.

class GWFUser(models.Model):
    name = models.CharField(max_length=100)
    login = models.CharField(max_length=50)
    email = models.EmailField(max_length=250, unique=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

