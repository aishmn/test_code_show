from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import gettext_lazy as _

# EmployerProfile = ContentType.objects.get( app_label='employer', model='employerprofile' )
# JobListing = ContentType.objects.get( app_label = 'jobs', model = 'job' )

User = get_user_model()

class Payment(models.Model):
    '''
        Possible payment methods ??
        - Send via Esewa/ Khalti/ ImePay
        - Perform Bank Transfer and send the transaction id
    '''
    user = models.ForeignKey(User, on_delete = models.SET_NULL,related_name='payments')
    remarks = models.CharField(max_length=300)
    amount = models.FloatField(_('Paid amount in Nepali Rupees'))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.first_name + self.created_at
    

