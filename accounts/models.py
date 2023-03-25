from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None  # Remove username field
    email = models.EmailField(_("email address"), unique=True)
    name = models.CharField(_("name"), max_length=100, blank=True, null=True)
    contact_email = models.EmailField(_("contact email"), blank=True, null=True)
    about = models.TextField(_("about"), blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
