from django.db import models
from django.contrib.auth.models import User
from .cook import Cook
from .category import Category

class Recipe(models.Model):
    """Model for Recipe"""

    name = models.CharField(max_length=50)
    description = models.TextField(blank = True, null=True)
    ingredients = models.TextField(blank = True, null=True)
    cook_time = models.IntegerField()
    instructions = models.TextField(blank = True, null=True)
    image = models.ImageField(upload_to=None, blank = True, null=True)

    """add id's to your db tables"""
    cook = models.ForeignKey(Cook, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = ("recipe")
        verbose_name_plural = ("recipes")