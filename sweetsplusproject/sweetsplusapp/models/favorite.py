from django.db import models
from django.contrib.auth.models import User
from .cook import Cook
from .recipe import Recipe

class Favorite(models.Model):
    """Model for Favorite"""
    """add id's to your db tables"""
    cook = models.ForeignKey(Cook, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.DO_NOTHING, blank=True, null=True)

    class Meta:
        verbose_name = ("favorite")
        verbose_name_plural = ("favorites")