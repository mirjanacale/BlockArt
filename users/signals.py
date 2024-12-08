from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
    This function is called by the post_save signal. The post_save signal is sent
    after an instance of the User model is saved. The function takes in the
    sender (the User model), the instance of the User model that was saved,
    and a created boolean that is True if the instance was created, False if
    it was only updated.
    If the instance was created, the function creates a Profile instance
    associated with the User instance.
    """
    if created:
        """
        If the User instance was created, create a Profile instance associated
        with the User. The Profile instance's user field is set to the User
        instance, and the Profile instance is then saved.
        """
        Profile.objects.create(user=instance, image='default.jpg')
        
        
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()        