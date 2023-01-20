from rest_framework import serializers
from ..models import EmployerProfile

class EmployerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployerProfile
        fields = 'user, address, phone_number'
        depth = 1
        read_only_fields = ['account_type']
