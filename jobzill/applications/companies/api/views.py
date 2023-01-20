from django.http import HttpResponse
from .serializer import  OrganizationSerializer
from ..models import Organization
from django.http import Http404
from rest_framework import permissions
from rest_framework import status
from rest_framework.views import APIView 
from rest_framework.response import Response


class CreateOrganizationView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, format= None):
        organizations = Organization.objects.all()
        serializer = OrganizationSerializer(organizations, many= True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request,format =None):
        serializer = OrganizationSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return  Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ManageOrganizationView(APIView):
    permission_classes = [permissions.AllowAny]
    def get_object(self, pk):
        try:
            return Organization.objects.get(pk=pk)
        except Organization.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        organization =self.get_object(pk)
        serializer = OrganizationSerializer(organization)
        return Response(serializer.data)

    def put(self, request, pk, format= None):
        organization=self.get_object(pk)
        serializer = OrganizationSerializer(organization, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status= status.HTTPS_400_BAD_REQUEST)

    def delete(self , request, pk, format=None):
        organization= self.get_object(pk)
        organization.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

