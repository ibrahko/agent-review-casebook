from django.db.models import F, Sum
from rest_framework import serializers

from .models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source="product.name")
    unit_price = serializers.IntegerField(source="product.unit_price")

    class Meta:
        model = OrderItem
        fields = ["product_name", "unit_price", "quantity"]


class OrderSerializer(serializers.ModelSerializer):
    customer_name = serializers.CharField(source="customer.name")
    customer_city = serializers.CharField(source="customer.city")
    items = OrderItemSerializer(many=True)
    total = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ["id", "customer_name", "customer_city", "items", "total"]

    def get_total(self, order):
        result = order.items.aggregate(total=Sum(F("quantity") * F("product__unit_price")))
        return result["total"] or 0
