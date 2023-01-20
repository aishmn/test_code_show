import uuid as uuid_lib

from .manager import CustomUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class BaseUser(AbstractUser):
    uuid = models.CharField(default=uuid_lib.uuid4,max_length=50,editable=False, primary_key=True)
    email = models.CharField(_('Email address'), max_length=250, unique=True)
    first_name = models.CharField(_('Firstname'), max_length=250)
    last_name = models.CharField(_('Lastname'), max_length=250)
    password = models.CharField(_('Password'), max_length=250)
    profile_image = models.FileField(
        upload_to="account/%Y/%m/%d/user/", null=True, blank=True, default=None)
    username = None
    isEmployer = models.BooleanField(default=False, verbose_name = _('Has Employer Profile'))
    isMember = models.BooleanField(default=False, verbose_name = _('Has Job Profile'))

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email + " " + self.get_full_name()
    

# common
# created_at
# updated_at

class Reset(models.Model):
    email = models.CharField(max_length=250)
    token = models.CharField(max_length=255, unique=True)