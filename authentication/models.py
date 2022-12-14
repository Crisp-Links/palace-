from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class User(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True, blank=True)
    first_name = models.CharField(max_length=50, null='True', blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    phone = models.PositiveIntegerField(null=True, blank=True)
    is_client = models.BooleanField(default=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email