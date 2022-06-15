from email.policy import default
from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.BigIntegerField()
    image = models.ImageField(upload_to='shop/', default='shop/default.png')
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


    
