from django.db import models

# Create your models here.
class Sample(models.Model):
    image = models.ImageField(upload_to='app/', blank=True)