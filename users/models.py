from django.db import models
from django.contrib.auth.models import User
import cloudinary
import cloudinary.models
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = cloudinary.models.CloudinaryField('image', default='default.jpg')

    def __str__(self):
        return f'{self.user.username} Profile'
    
# Automatically create a profile when a user is created
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        print("Profile created for user:", instance.username)
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()    