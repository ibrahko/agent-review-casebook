from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)


class Product(models.Model):
    name = models.CharField(max_length=100)
    unit_price = models.PositiveIntegerField(help_text="Price in FCFA")


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="orders")
    created_at = models.DateTimeField(auto_now_add=True)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
