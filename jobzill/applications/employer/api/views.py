from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions
from django.db.models.query import QuerySet
from ..models import EmployerProfile
from .serializers import *

class EmployerProfileLCView(ListCreateAPIView):
    permissions_classes = [ permissions.isAuthenticatedOrReadOnly ]
    serializer_class = EmployerProfileSerializer
    queryset = EmployerProfile.objects.all()

    # Handle employer profile creation and upgrade as per the payments

class EmployerProfileRUDView(RetrieveUpdateDestroyAPIView):
    permissions_classes = [ permissions.isAuthenticatedOrReadOnly ]
    serializer_class = EmployerProfileSerializer
    queryset = EmployerProfile.objects.all()

    def get_queryset(self):
        queryset = self.queryset
        user = self.request.user
        if isinstance(queryset, QuerySet):
            queryset.filter(user = user)
        return queryset