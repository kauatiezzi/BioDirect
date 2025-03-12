from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    custom_url = models.CharField(max_length=255, unique=True)
    photo = models.ImageField(upload_to='profiles/', null=True, blank=True)
    instagram = models.URLField(max_length=255, null=True, blank=True)
    whatsapp = models.URLField(max_length=255, null=True, blank=True)
    linkedin = models.URLField(max_length=255, null=True, blank=True)
    nome_empresa = models.CharField(max_length=255, null=True, blank=True)
    theme_color = models.CharField(max_length=7, default='#ffffff')

    def __str__(self):
        return self.user.username
    
class Button(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    url = models.URLField(max_length=255)

    def __str__(self):
        return self.name

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance, custom_url=slugify(instance.username))
    else:
        instance.userprofile.save()
