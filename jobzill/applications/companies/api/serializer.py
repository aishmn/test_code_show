from ..models import Organization
from rest_framework import serializers

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model =Organization
        fields =("id","name","logo","location","size","category","job_posts","description")