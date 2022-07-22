from django.db import models

# Create your models here.
class search(models.Models):
    title = models.CharField(max_length=150)
    image = models.ImageField(blank=True)
