from django.db import models
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

from core.models import TimeStampedModel

class CustomUserManager(BaseUserManager):
    def create_user(self, username, password, email=''):
        if not username:
            raise ValueError('Username is required')
    
        user = self.model(username=username, email=email)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, email=''):
        user = self.create_user(username, password, email)
        user.is_superuser = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin, TimeStampedModel):
    is_active = models.BooleanField('Activation status', default=True)
    username = models.CharField('User ID', max_length=255, unique=True)
    name = models.CharField('name', blank=True, max_length=125)
    email = models.EmailField('email', max_length=255, blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ()
    objects = CustomUserManager()

    class Meta:
        verbose_name = 'member'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    @property
    def is_staff(self):
        return self.is_superuser



