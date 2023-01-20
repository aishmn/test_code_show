from rest_framework import serializers
from ..models import Payment

class PaymentSerializer():
    class Meta:
        model = Payment
        fields = '__all__'