from rest_framework import serializers
from auth.serializers import UserSerializer
from api.models import Product, Order, DeliveryCenter, Delivery

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price']

class OrderSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    product = ProductSerializer()
    class Meta:
        model = Order
        fields = ['id', 'user', 'product', 'quantity']

class DeliveryCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryCenter
        fields = ['id', 'name']

class DeliverySerializer(serializers.ModelSerializer):
    order = OrderSerializer()
    class Meta:
        model = Delivery
        fields = ['id', 'order', 'delivery_center', 'received_at', 'delivered_at']

