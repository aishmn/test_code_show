from django.db import models
from django.utils.translation import  gettext_lazy as _

class Organization(models.Model):
    name=models.CharField(_("name"), max_length=250,)
    logo = models.FileField(_("logo"),upload_to="organization/%Y/%D/%M/user/",null=True,blank=True,default=None)
    location =models.CharField(_("location"),max_length=250,null=True)
    size= models.CharField(max_length=250)
    category = models.CharField(max_length=250, default=None, null=True)
    description = models.TextField(max_length=250, null=True)
    job_posts = models.TextField(_("job posts"),max_length=250, null=True)
    #name
    #logo
    #location
    #size
    #category
    #description
    #job Posts

    def __str__(self):
        return self.name 