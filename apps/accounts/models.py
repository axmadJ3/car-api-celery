from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import UserManager

class CustomUser(AbstractBaseUser, PermissionsMixin, models.Model):
    phone_number = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'phone_number'
    
    def save(self, *args, **kwargs):
        self.phone_number = self.phone_number.replace('+', '').replace(' ', '')
        
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.phone_number
    
    objects = UserManager()