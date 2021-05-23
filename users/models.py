from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin, BaseUserManager)
from django.utils import timezone
# Create your models here.



class CustomizeUserManager(BaseUserManager):
    def create_superuser(self, email, username, password, phone, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser',True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('superuser is_staff must be True')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('superuser is_superuser must be True')
        return self.create_user(email, username, phone, password, **other_fields)

    def create_user(self, email, username, password, phone, **other_fields):
        if not email:
            raise ValueError('User Must Have An email address ')
        
        email = self.normalize_email(email)
        user = self.model(email=email, password=password, phone=phone, **other_fields)
        user.set_password(password)
        user.save()
        return user
    



class CustomizeUserModel(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('email', unique=True)
    username = models.CharField('username',max_length=255, blank=True, null=True)
    start_date = models.DateTimeField('start_date', default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    phone = models.CharField('Phone', max_length=255)
    objects = CustomizeUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'phone']




class UserProfileModel(models.Model):
    user = models.ForeignKey(to=CustomizeUserModel, on_delete=models.CASCADE)
    first_name = models.CharField('first_name', max_length=255)
    last_name = models.CharField('last_name', max_length=255)
    phone = models.CharField('phone', null=True, blank=True, max_length=255)
    address = models.CharField('address',max_length=300, blank=True, null=True)
    start_date = models.DateField('start_date', default=timezone.now) 

class FactoryProfileModel(models.Model):
    user = models.ForeignKey(to=CustomizeUserModel, on_delete=models.CASCADE)
    rep_name = models.CharField('name', max_length=255)
    address = models.CharField('address',max_length=255)
    rep_phone = models.CharField('phone',max_length=255)


class OfficeProfileModel(models.Model):
    user = models.ForeignKey(to=CustomizeUserModel, on_delete=models.CASCADE)
    rep_name = models.CharField('name', max_length=255)
    address = models.CharField('address',max_length=255)
    rep_phone = models.CharField('phone',max_length=255)

