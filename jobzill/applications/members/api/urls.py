from django.urls import path
from .views import *

urlpatterns = [
    path('',JobProfileLCView.as_view()),
    path('<int:id>',JobProfileRUDView.as_view()),
    path('skill',SkillLCView.as_view()),# Make this user specific
    path('skill/<int:id>',SkillRUDView.as_view()),
    path('experience',ExperienceLCView.as_view()),# Make this user specific
    path('experience/<int:id>',ExperienceRUDView.as_view()),

]