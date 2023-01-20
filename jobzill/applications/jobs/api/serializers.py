from rest_framework import serializers
from ..models import Job, Category

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['location','description','timing','experience', 'type','title','industry','salary','slug']
        read_only_fields = ['created_at','updated_at']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'