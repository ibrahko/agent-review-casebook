import random

from django.core.management.base import BaseCommand
from django.db import transaction

from orders.models import Customer, Order, OrderItem, Product


class Command(BaseCommand):
    help = "Fill the database with demo data (deterministic)."

    @transaction.atomic
    def handle(self, *args, **options):
        if Order.objects.exists():
            self.stdout.write("Demo data already present.")
            return
        rng = random.Random(42)
        cities = ["Bamako", "Ségou", "Sikasso", "Mopti", "Kayes"]
        customers = Customer.objects.bulk_create(
            Customer(name=f"Customer {i}", city=rng.choice(cities)) for i in range(50)
        )
        products = Product.objects.bulk_create(
            Product(name=f"Product {i}", unit_price=rng.randint(100, 5000)) for i in range(30)
        )
        orders = Order.objects.bulk_create(Order(customer=rng.choice(customers)) for _ in range(200))
        OrderItem.objects.bulk_create(
            OrderItem(order=o, product=rng.choice(products), quantity=rng.randint(1, 5))
            for o in orders
            for _ in range(3)
        )
        self.stdout.write("Created 50 customers, 30 products, 200 orders, 600 items.")
