from django.db import models

# Create your models here.

class Slider(models.Model):
    url = models.URLField()
    image = models.ImageField(upload_to="")
    