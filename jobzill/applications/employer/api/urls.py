from django.urls import path
from .views import *

urlpatterns = [
    path('',EmployerProfileLCView.as_view()),
    path('<int:id>',EmployerProfileRUDView.as_view()),
]