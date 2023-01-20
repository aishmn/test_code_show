import uuid as uuid_lib
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save

User = get_user_model()

class EmployerProfile(models.Model):
    class EMP_TYPE(models.TextChoices):
        BASIC = 1, "Basic"
        GOLD = 2, "Gold"
        PLATINUM = 3, "Platinum"

    user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name=_('User Info'),related_name='employerprofile')
    address = models.CharField(_('Title'), max_length=90, blank = True) # find a better address solution
    phone_number = models.CharField(_('Title'), max_length=90, blank = True) # validate this
    account_type = models.CharField(max_length=20,choices=EMP_TYPE.choices,default=EMP_TYPE.BASIC)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #payments
    #companies

    def __str__(self):
        
        return self.user.get_full_name
