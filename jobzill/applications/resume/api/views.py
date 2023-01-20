# from rest_framework.generics import APIListCreateView, APIRetrieveUpdateDestroyView
# from .serializers import ResumeSerializer
# from ..models import Resume
# from .. import permissions as CustomPermissions
# from rest_framework import permissions
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from django.http import HttpResponse

# class ResumeLCView(APIListCreateView):
#     permission_classes = [ CustomPermissions.WriteOnly | permissions.IsAdminUser ]
#     serializer_class = ResumeSerializer
#     queryset = Resume.objects.all()

# class ResumeRUDView(APIRetrieveUpdateDestroyView):
#     serializer_class = ResumeSerializer
#     queryset = Resume.objects.all()

# #

# class ResumeBuildView(View):
#     def get(self,request):
        
#         return HttpResponse()
