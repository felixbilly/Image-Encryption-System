"""
from django.db import models

# Create your models here.
from django.db import models

class EncryptedImage(models.Model):
    image = models.ImageField(upload_to='images/')
    encrypted_image = models.BinaryField()

class DecryptedImage(models.Model):
    encrypted_image = models.ForeignKey(EncryptedImage, on_delete=models.CASCADE)
    decrypted_image = models.BinaryField()
"""

    # models.py
from django.db import models
from django.contrib.auth.models import User


class profile(models.Model):
    User= models.OneToOneField(User, null=True, on_delete=models.CASCADE )
    def _str_(self):
     return str(self.user)

# class EncryptedImage(models.Model):
#     image = models.ImageField(upload_to='encrypted_images/')
#     key = models.CharField(max_length=20, )  # Store the encryption key as binary data

class Result(models.Model):
   key=models.CharField(max_length=20 , blank=False)
   image= models.ImageField(upload_to='images',default='profile.png')
   encrypted_image= models.ImageField(upload_to='images',null = True, default='encryted.png')

  