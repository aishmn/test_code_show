# from django.db import models
# from django.contrib.contenttypes.models import ContentType

# EmployerProfile = ContentType.objects.get( app_label='employer', model='employerprofile' )
# Job = ContentType.objects.get( app_label='jobs', model='job' )
# Resume = ContentType.objects.get( app_label='resume', model='resume' )
# CoverLetter = ContentType.objects.get( app_label='coverletter', model='coverletter' )

# class JobApplication(models.Model):
#     profile = models.ForeignKey(EmployerProfile, on_delete=models.SET_NULL)
#     job = models.ForeignKey(Job, on_delete=models.SET_NULL)
#     resume = models.ForeignKey(Resume, on_delete=models.SET_NULL)
#     cover_letter = models.ForeignKey(CoverLetter, on_delete=models.SET_NULL)
#     date = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.profile.user.get_full_name() + str(self.date)