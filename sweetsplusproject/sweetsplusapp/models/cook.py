from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Cook(models.Model):
    """Model for the Cook """

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("cook")
        verbose_name_plural = ("cooks")

# Every time a `User` is created, a matching `Cook`
# object will be created and attached as a one-to-one
# property
@receiver(post_save, sender=User)
def create_cook(sender, instance, created, **kwargs):
    if created:
        Cook.objects.create(user=instance)

# Every time a `User` is saved, its matching `Cook`
# object will be saved.
@receiver(post_save, sender=User)
def save_cook(sender, instance, **kwargs):
    instance.cook.save()