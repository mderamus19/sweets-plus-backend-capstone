from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    """Model for the Category"""

    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("category")
        verbose_name_plural = ("categories")