
# code
from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile
from store.models import UploadFile
  
  
@receiver(post_save, sender=User) 
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile ='profile_pics/default-avatar.png'
        Profile.objects.create(user=instance)
   
@receiver(post_save, sender=User) 
def save_profile(sender, instance, **kwargs):
        instance.profile.save()
        

        
@receiver(post_save, sender=User) 
def create_upload(sender, instance, created, **kwargs):
    if created:
        UploadFile.objects.create(user=instance)
   

@receiver(post_save, sender=User) 
def save_upload(sender, instance, **kwargs):
        instance.uploadfile.save()
