# from django.db import models
# from django.contrib.contenttypes.models import ContentType
# from django.utils.translation import  gettext_lazy as _

# JobProfile = ContentType.objects.get( app_label='member', model='jobprofile' )

# class Resume(models.Model):
#     profile = models.ForeignKey( JobProfile, related_name='resume', on_delete= models.CASCADE )
#     file = models.FileField( _('Resume file'), upload_to="member/%Y/%D/%M/user/")
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.profile.user.first_name + self.id