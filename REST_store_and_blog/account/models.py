from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.

class AccountModelManager(BaseUserManager):
    
    def create_user(self, email, name, password=None):
        
        if not email:
            raise ValueError('User must have a email address.')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):

        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user

class AccountModel(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(unique=True, max_length=256)
    name = models.CharField(max_length=256)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = AccountModelManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_fullname(self):

        """ Retrieve name of user """

        return self.name

    def __str__(self):

        """ Retrieve email of user """

        return self.email