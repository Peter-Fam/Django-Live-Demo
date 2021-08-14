from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class APIUser(AbstractUser):
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    email = models.EmailField(_("User Email"), unique=True)
    objects = CustomUserManager()

    def __str__(self):
        return self.username
