from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from ..models import Job, Category
from .serializers import JobSerializer, CategorySerializer
from .. import permissions as CustomPermissions
from rest_framework import filters,pagination, permissions
from django.db.models.query import QuerySet

class JobListView(ListAPIView):
    pagination_class = pagination.LimitOffsetPagination
    queryset = Job.objects.filter(is_active = True)
    serializer = JobSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']
    permission_classes  = [ permissions.AllowAny ]

class JobCreateAPIView(CreateAPIView):
    permission_classes  = [ CustomPermissions.JobPostPermission ]
    queryset = Job.objects.all()
    serializer = JobSerializer

class JobRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permissions_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Job.objects.all()
    serializer = JobSerializer

    def get_queryset(self):
        queryset = self.queryset
        user = self.request.user
        if isinstance(queryset, QuerySet):
            pass
            # Filter it to show only to the employer account associated with the respective company
            #  queryset = queryset.filter(posted_by)
        return queryset


class JobCategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer = CategorySerializer
    permission_classes  = [ permissions.IsAuthenticatedOrReadOnly ]

class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer = CategorySerializer
    permission_classes  = [ permissions.IsAdminUser ]
    pagination_class = pagination.LimitOffsetPagination
