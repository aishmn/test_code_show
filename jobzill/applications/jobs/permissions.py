import datetime
from rest_framework.permissions import BasePermission
from django.contrib.contenttypes.models import ContentType

# EmployerProfile = ContentType.objects.get( app_label='employer', model='employerprofile' )
# JobListing = ContentType.objects.get( app_label = 'jobs', model = 'job' )

class JobPostPermission(BasePermission):
    def has_permission(self, request, view):
        try:
            profile = EmployerProfile.objects.get(user = request.user)

            limit = 0

            # Change to switch case ??
            
            # if( profile.account_type == EmployerProfile.Emp_Type.BASIC ):
            #     limit = 5
            
            # elif( profile.account_type == EmployerProfile.Emp_Type.GOLD ):
            #     limit = 20
            
            # elif( profile.account_type == EmployerProfile.Emp_Type.Platinum ):
            #     limit = 100

            # myposts_this_week = JobListing.objects.count(posted_by = profile, created_at__gte = datetime.datetime.now() - datetime.timedelta(days = 7))
            
            # if( myposts_this_week <= limit ):
            #     return True

            return False

        except:
            return False
