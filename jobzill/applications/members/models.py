import uuid as uuid_lib
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save

User=get_user_model()

class Skill(models.Model):
    name = models.CharField(_('Title'), max_length= 30)
    category = models.CharField(_('Type of skill'), max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class JobProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_('User Info'), related_name='jobprofile')
    title = models.CharField(_('Title'), max_length=90, blank=True)
    description = models.TextField(_('Personal Descripton'), max_length=500, blank = True) # Handle the limit in frontend
    address = models.CharField(_('Title'), max_length=90, blank = True) # find a better address solution
    skills = models.ManyToManyField(Skill,related_name='profiles')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #Experience

    def __str__(self):
        return self.user.get_full_name

class Experience(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('Work Experience'))
    title = models.CharField(_('Title'), max_length=90)
    # company = models.ForeignKey('Company', on_delete=models.CASCADE, verbose_name=_('experience'))
    running = models.BooleanField(default=False, verbose_name=_('Still going on ?'))
    start_date = models.DateField()
    end_date = models.DateField()
    
    def __str__(self):
        return self.person.first_name + self.title + self.company
