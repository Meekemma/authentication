# models.py
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models



#Create your models here.
class UserManager(BaseUserManager):
    def create_user (self, email, username, password=None):

        """
        Creates, saves and return a User with the given email, username, and password.
        """

        if not email:
            raise ValueError('user must have an email address')
        if not username:
            raise ValueError('user must have a username')

        user =self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username,password=None):
        """
        Creates, saves, and returns a superuser with the given email, username, and password.
        """

        if password is None:
            raise ValueError('Password should not be none')
        
        user = self.create_user(email, username, password)
        user.is_superuser =True
        user.is_staff = True
        user.save()
        return user


# Custom User model with email as the unique identifier
class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True, db_index=True)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'  # Email used as the login identifier
    REQUIRED_FIELDS = ['username']

    objects = UserManager()  # Custom manager for the User model


    def __str__(self):
      return self.email
    
