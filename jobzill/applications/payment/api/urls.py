from django.urls import path
from .views import PaymentRUDView, PaymentLCView

urlpatterns = [
    path('',PaymentLCView.as_view()),
    path('/<str:pk>',PaymentRUDView.as_view())
]