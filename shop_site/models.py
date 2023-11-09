from django.db import models
from django.conf import settings
from .mixins import *
from django.urls import reverse
# Create your models here.

class Shop(models.Model):
    title = models.CharField(max_length=250, verbose_name="Тема")
    
    def __str__(self):
        return f'{self.title}'
    
class Contacts (TimestampMixin, models.Model):
    firstname = models.CharField(max_length=250)
    lastname = models.CharField(max_length=250)
    number = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    message = models.CharField(max_length=250)

    def get_absolute_url(self): 
        return reverse('index')
    
class Workers(models.Model):
    fullname = models.CharField(max_length=250)
    position = models.CharField(max_length=250)
    avatar = models.ImageField()

class Reviews(models.Model):
    fullname = models.CharField(max_length=250)
    position = models.CharField(max_length=250)
    message = models.CharField(max_length=250)
    avatar = models.ImageField()

class Blogs(models.Model):
    title = models.CharField(max_length=250)
    text = models.TextField()
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

class Category(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(null=True, blank=True)
    description = models.CharField(max_length=250)

class Brands(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(null=True, blank=True)
    description = models.CharField(max_length=250)

class Products(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    image = models.ImageField()
    price = models.FloatField()
    color = models.CharField(max_length=250)
    weight = models.FloatField()
    barcode = models.CharField(max_length=250)
    categoryObject = models.ForeignKey(Category, on_delete=models.CASCADE)
    brandObject = models.ForeignKey(Brands, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class ProductsImages(models.Model):
    productObject = models.ForeignKey(Products, on_delete=models.CASCADE)
    image = models.ImageField()

class ProductsLikes(models.Model):
    productObject = models.ForeignKey(Products, on_delete=models.CASCADE)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

class ProductsRaitings(models.Model):
    productObject = models.ForeignKey(Products, on_delete=models.CASCADE)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    points = models.IntegerField()

class Subscriptions(models.Model):
    mail = models.TextField(max_length=250)