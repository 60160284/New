from typing import Sized
from django.db import models

from django.urls import reverse
from django.http import FileResponse
from django.contrib.auth.forms import User
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.template.defaultfilters import default, slugify
from django.db.models.signals import pre_save, post_save
from autoslug import AutoSlugField
from .utils import unique_slug
from PIL import Image
#CATEGORY = (
	#('itd', 'IT Development'),
	#('wd', 'Web Design'),
	#('iandd', 'Illustration and Drawing'),
	#('sm', 'Social Media'),
	#('ps', 'PhotoShop'),
	#('crypto', 'CryptoCurrencies'),
	#) ทางเลือกใหม่

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=255,unique=True)
    slug=models.SlugField(max_length=255,unique=True)

    def __str__(self):
        return self.name

    
    class Meta :
        ordering=('name',)
        verbose_name ='หมวดหมู่'
        verbose_name_plural = "ข้อมูลหมวดหมู่"

    def get_url(self):
        return reverse('product_by_category',args=[self.slug])

class Typefile(models.Model):
    name=models.CharField(max_length=255,unique=True)
    slug=models.SlugField(max_length=255,unique=True)
      
    
    def __str__(self):
        return self.name
    class Meta :
        ordering=('name',)
        verbose_name ='รูปแบบ'
        verbose_name_plural = "ข้อมูลรูปแบบ"


    def get_url(self):
        return reverse('product_by_typefile',args=[self.slug])

class Published(models.Model):
    name=models.CharField(max_length=255,unique=True)
    slug=models.SlugField(max_length=255,unique=True)
      
    def __str__(self):
        return self.name

    class Meta :
        ordering=('name',)
        verbose_name ='การเผยแพร่'
        verbose_name_plural = "ข้อมูลการเผยแพร่"

    def get_url(self):
        return reverse('product_by_published',args=[self.slug])



class UploadFile(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=255,unique=True)

    slug = AutoSlugField(populate_from='name',editable=True, unique_with='user')

    description=models.TextField(blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    typefile=models.ForeignKey(Typefile,on_delete=models.CASCADE)
    published=models.ForeignKey(Published,on_delete=models.CASCADE)
    
    inputfile=models.FileField(upload_to='user/inputfile/', null=True, blank=True)
    image=models.ImageField(upload_to='user/cover/', null=True, blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2, default=0.0)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
   
    
    def __str__(self):
        return f'{self.name}'




    def get_url(self, *args):
        return reverse('uploadProductDetail',args=[self.category.slug,self.slug])
        
       
    def get_absolute_url(self): # new
	    return reverse('store:uploadProductDetail', kwargs={'slug':self.slug})

def pre_save_slug_field(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug(instance)

pre_save.connect(pre_save_slug_field, sender=UploadFile)

class Profile(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        profile_image = models.ImageField(default="img/default.jpg" ,upload_to='profile_pics/')

   
        def __str__(self):
            return f'{self.user.username} Profile'

        def save(self):
            super().save()

            img= Image.open(self.profile_image.path)


        def get_url(self, *args):
            return reverse('profileDetail',args=[self.user.profile])




       