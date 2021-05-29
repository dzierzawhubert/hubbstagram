from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UsersProfile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        UsersProfile.objects.create(user=instance, description='default', name='default', sec_name="default", email=instance.email)
        print('You have now default profile related to your account')
