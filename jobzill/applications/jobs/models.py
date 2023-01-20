from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import pre_save
from django.template.defaultfilters import slugify
import string, random
# from asgiref.sync import sync_to_async

from jobzill.applications.employer.models import EmployerProfile

# async def getModel(obj):
#     modelclass =await obj.model_class()
#     return modelclass

# EmployerProfile = ContentType.objects.get(app_label='employer', model='employerprofile')
# Company = ContentType.objects.get(app_label = 'companies', model = 'Company')

class Job(models.Model):
    #logo
    class JOB_TYPE(models.TextChoices):
        PHYSICAL = 1,"Physical"
        REMOTE = 2,"Remote"

    location = models.CharField(verbose_name = _('Job Location'), max_length=100)
    description = models.TextField(max_length=500, verbose_name=_('Job Description'))
    timing = models.CharField(verbose_name = _('Job Time'), max_length=100)
    experience = models.CharField(verbose_name = _('Experience'), max_length=100)
    type = models.CharField(max_length=20,choices=JOB_TYPE.choices,default=JOB_TYPE.PHYSICAL)
    title = models.CharField(verbose_name = _('Job Title'), max_length=100)
    industry = models.CharField(verbose_name = _('Industry'), max_length=100)
    # company = models.ForeignKey(Company, on_delete = models.CASCADE,related_name = 'jobs')
    posted_by = models.ForeignKey(EmployerProfile, related_name='jobposts', on_delete= models.CASCADE)
    is_active = models.BooleanField(default = True)
    salary = models.CharField(verbose_name = 'Salary Offered', max_length = 100)
    category = models.ManyToManyField('Category',verbose_name=_('Job Cateogry'),related_name='jobs')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.CharField(max_length = 200, null = True, blank = True)

    def __str__(self):
        return self.title

class Category(models.Model):
    subcategory_of = models.ForeignKey('Category', on_delete=models.SET_NULL, null = True, blank = True, related_name='childrencategory')
    name = models.TextField(max_length=50,verbose_name=_('Job Category name'))

    def __str__(self):
        return "Caategory: " + self.name


def random_string_generator(size = 10, chars = string.ascii_lowercase + string.digits): 
    return ''.join(random.choice(chars) for _ in range(size)) 
 
def unique_slug_generator(instance, new_slug = None): 
    if new_slug is not None: 
        slug = new_slug 
    else: 
        slug = slugify(instance.title) 
        Klass = instance.__class__ 
        qs_exists = Klass.objects.filter(slug = slug).exists() 

    if qs_exists:
        new_slug = "{slug}-{randstr}".format( 
        slug = slug, randstr = random_string_generator(size = 4)) 
        return unique_slug_generator(instance, new_slug = new_slug)

    return slug 

def pre_save_receiver(sender, instance, *args, **kwargs): 
    if not instance.slug: 
        instance.slug = unique_slug_generator(instance) 

pre_save.connect(pre_save_receiver, sender = Job) 
