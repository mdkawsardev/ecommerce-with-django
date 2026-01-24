from django.db import models

class Sample(models.Model):
    image = models.ImageField(upload_to='images', blank=True)

class Product(models.Model):
    title = models.CharField(max_length=222)
    desc = models.TextField()
    product_image = models.ImageField(upload_to='images', blank=True)