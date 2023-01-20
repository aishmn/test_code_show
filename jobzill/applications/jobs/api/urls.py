from django.urls import path
from .views import JobListView, JobCreateAPIView, JobRetrieveUpdateDestroyAPIView, JobCategoryListCreateAPIView, CategoryRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('', JobListView.as_view()),
    path('create', JobCreateAPIView.as_view()),
    path('<str:pk>', JobRetrieveUpdateDestroyAPIView.as_view()),
    path('cateogry', JobCategoryListCreateAPIView.as_view()),
    path('category/<str:pk>', CategoryRetrieveUpdateDestroyAPIView.as_view())
]