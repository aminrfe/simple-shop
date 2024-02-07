from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

class DeliveryCenter(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Delivery(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    delivery_center = models.ForeignKey(DeliveryCenter, on_delete=models.CASCADE)
    received_at = models.DateTimeField(auto_now_add=True)
    delivered_at = models.DateTimeField(null=True)
