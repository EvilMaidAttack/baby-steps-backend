from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from .managers import AppUserManager

class AppUser(AbstractUser):

    username = None
    email = models.EmailField((_("E-Mail")), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = AppUserManager()

    def __str__(self) -> str:
        return self.email 
