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

class EncryptedImage(models.Model):
    image = models.ImageField(upload_to='encrypted_images/')
    key = models.BinaryField()  # Store the encryption key as binary data