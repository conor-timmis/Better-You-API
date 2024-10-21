from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django_resized import ResizedImageField

class Profile(models.Model):
    """
    Profile model class: When User is created,
    the Profile is created (OneToOneField)
    """
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True)
    image = ResizedImageField(
        size=[300, 300], quality=75, upload_to='profiles/',
        default='../default_profile_rgvmnf', blank=True
    )
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s profile"

def create_profile(sender, instance, created, **kwargs):
    """
    Create Profile function: Owner is assigned
    upon creation of Profile
    """
    if created:
        Profile.objects.create(owner=instance)

post_save.connect(create_profile, sender=User)