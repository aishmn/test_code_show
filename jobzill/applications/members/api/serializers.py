from rest_framework import serializers
from ..models import Skill, Experience, JobProfile


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'


class JobProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobProfile
        fields = '__all__'