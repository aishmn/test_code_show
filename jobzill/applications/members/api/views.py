from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions, filters, pagination
from ..models import Skill, Experience, JobProfile
from .serializers import *

class SkillLCView(ListCreateAPIView):
    serializer_class = SkillSerializer
    queryset = Skill.objects.all()

class SkillRUDView(RetrieveUpdateDestroyAPIView):
    serializer_class = SkillSerializer
    queryset = Skill.objects.all()


class ExperienceLCView(ListCreateAPIView):
    serializer_class = ExperienceSerializer
    queryset = Experience.objects.all()

class ExperienceRUDView(RetrieveUpdateDestroyAPIView):
    serializer_class = ExperienceSerializer
    queryset = Experience.objects.all()

class JobProfileLCView(ListCreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = JobProfileSerializer
    queryset = JobProfile.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']
    pagination_class = pagination.LimitOffsetPagination

class JobProfileRUDView(RetrieveUpdateDestroyAPIView):
    serializer_class = JobProfileSerializer
    queryset = JobProfile.objects.all()
