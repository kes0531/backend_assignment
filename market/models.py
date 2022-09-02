from django.db import models

# Create your models here.

class Profile(models.Model):
    member_id = models.CharField(max_length=25)
    member_pw = models.CharField(max_length=30)
    member_name = models.CharField(max_length=20)
    member_photo = models.ImageField(upload_to="member_photo")

class Product(models.Model):
    pid = models.UUIDField(primary_key=True)
    product_name = models.CharField(max_length=100)
    product_price = models.IntegerField()
    product_createdDate = models.DateTimeField(auto_now_add=True)
    product_modifiedDate = models.DateTimeField(auto_now=True)
    product_image = models.ImageField(upload_to="product_image")

class Order(models.Model):
    order_id = models.UUIDField(primary_key=True)
    order_createdDate = models.DateTimeField(auto_now_add=True)
    order_modifiedDate = models.DateTimeField(auto_now=True)