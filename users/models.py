from django.db import models
from django.contrib.auth.models import User
import cloudinary
import cloudinary.models
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = cloudinary.models.CloudinaryField('image', default='default.jpg')

    def __str__(self):
        return f'{self.user.username} Profile'