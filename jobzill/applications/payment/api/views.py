from rest_framework.views import APIListCreateView, APIRetrieveUpdateDestroyView
from .serializers import PaymentSerializer
from ..models import Payment

class PaymentLCView(APIListCreateView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()

class PaymentRUDView(APIRetrieveUpdateDestroyView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()