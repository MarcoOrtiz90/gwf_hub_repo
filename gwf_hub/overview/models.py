from django.db import models
from django.db.models.fields import TextField
from django.db.models.deletion import CASCADE

# Create your models here.
class TestFlow(models.Model):
    flow_id = models.CharField(max_length=50)
    available = models.BooleanField(default=True)
    owner = models.CharField(max_length=50)

    def __str__(self):
        return self.flow_id