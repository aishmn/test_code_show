
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from .models import JobProfile

User=get_user_model()


def save_profile(sender, instance,created, **kwargs):
    print("Running post save signal__________________---",sender,instance,created, kwargs)
    # Create job profile on user save\
    if created:
        profile = JobProfile(user = instance)
        profile.save()


post_save.connect(save_profile, sender = User)