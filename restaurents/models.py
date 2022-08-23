from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django_mysql.models import DynamicField, Model
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.hashers import make_password

class UserManager(BaseUserManager):
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

        return self.create_user( user_name, password,**other_fields)
    
    def create_user(self, user_name, password,**other_fields):

        user = self.model(user_name=user_name,
                          **other_fields)
        user.set_password(password)
        user.save()
        return user


class NewUser(AbstractBaseUser, PermissionsMixin):
    user_name = models.CharField(max_length=150, unique=True)
    email=models.EmailField(max_length=100,null=True,blank=True)
    password=models.CharField(max_length=15)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser=models.BooleanField(default=False)

    USERNAME_FIELD = 'user_name'
    objects = UserManager()
    REQUIRED_FIELDS = ['password']

    def save(self, *args, **kwargs):
        if not self.is_superuser:
            self.password = make_password(self.password)
        # super().full_clean()
        super().save(*args, **kwargs)

    


class restaurants(models.Model):
    restaurants_name=models.CharField(max_length=150, unique=True)
    restaurants_location=models.CharField(max_length=150, unique=True)

class otp(models.Model):
    otpdata=models.CharField(max_length=6, unique=True)
    user=models.ForeignKey(
        NewUser, on_delete=models.CASCADE, null=True, blank=True
    )


# class FormField(Model):
#     user=models.ForeignKey(
#         NewUser, on_delete=models.CASCADE, null=True, blank=True
#     )

#     attrs = DynamicField(
#         spec={
#             "size": str,
#         }
#         )
