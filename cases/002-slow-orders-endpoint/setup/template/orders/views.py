from rest_framework import generics

from .models import Order
from .serializers import OrderSerializer


class OrderList(generics.ListAPIView):
    queryset = Order.objects.all().order_by("id")
    serializer_class = OrderSerializer
