# todo/todo_api/urls.py : API urls.py
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateOrganizationView, ManageOrganizationView

urlpatterns = [
    path('', CreateOrganizationView.as_view()),
    path('<int:pk>',ManageOrganizationView.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)