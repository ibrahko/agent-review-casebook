from django.test import TestCase

from .models import Customer, Order, OrderItem, Product


class OrderListTests(TestCase):
    def setUp(self):
        customer = Customer.objects.create(name="Awa", city="Bamako")
        rice = Product.objects.create(name="Rice", unit_price=500)
        millet = Product.objects.create(name="Millet", unit_price=300)
        order = Order.objects.create(customer=customer)
        OrderItem.objects.create(order=order, product=rice, quantity=2)
        OrderItem.objects.create(order=order, product=millet, quantity=1)

    def test_lists_orders_with_items_and_total(self):
        response = self.client.get("/api/orders/")
        self.assertEqual(response.status_code, 200)
        [order] = response.json()
        self.assertEqual(order["customer_name"], "Awa")
        self.assertEqual(len(order["items"]), 2)
        self.assertEqual(order["total"], 1300)
