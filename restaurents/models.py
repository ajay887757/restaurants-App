from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class CustomAccountManager(AbstractBaseUser):
    def create_superuser(self, user_name, password,**other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user( user_name, password,  **other_fields)
    
    def create_user(self, user_name, password, **other_fields):

        user = self.model(user_name=user_name,
                          **other_fields)
        user.set_password(password)
        user.save()
        return user


class NewUser(models.Model):
    user_name = models.CharField(max_length=150, unique=True)
    email=models.EmailField(max_length=100,null=True,blank=True)
    password=models.CharField(max_length=15)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser=models.BooleanField(default=False)

    USERNAME_FIELD = 'user_name'
    objects = CustomAccountManager()
    REQUIRED_FIELDS = ['password']

    def __str__(self):
        return self.user_name


class restaurants(models.Model):
    restaurants_name=models.CharField(max_length=150, unique=True)
    restaurants_location=models.CharField(max_length=150, unique=True)

class otp(models.Model):
    otpdata=models.CharField(max_length=6, unique=True)
    user=models.ForeignKey(
        NewUser, on_delete=models.CASCADE, null=True, blank=True
    )