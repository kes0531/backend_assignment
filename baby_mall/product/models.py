from django.db import models

class Product(models.Model):
    pid = models.IntegerField(primary_key=True)
    name = models.TextField()
    price = models.IntegerField()
    createdDate = models.DateTimeField(auto_now_add=True)
    modifiedDate = models.DateTimeField(auto_now=True)
    image = models.ImageField(blank=True)
