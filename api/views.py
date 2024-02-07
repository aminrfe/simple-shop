from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from api.models import *
from api.serializers import *
from api.serializers import *

class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        queryset = Order.objects.all()
        serializer = OrderSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        data = request.data
        order = Order.objects.create(
            user_id=data['user'],
            product_id=data['product'],
            quantity=data['quantity']
        )
        serializer = OrderSerializer(order)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        queryset = Order.objects.all()
        order = get_object_or_404(queryset, pk=pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data)
    
    def update(self, request, pk=None):
        order = Order.objects.get(pk=pk)
        data = request.data
        order.user_id = data['user']
        order.product_id = data['product']
        order.quantity = data['quantity']
        order.save()
        serializer = OrderSerializer(order)
        return Response(serializer.data)
    
    def destroy(self, request, pk=None):
        order = Order.objects.get(pk=pk)
        order.delete()
        return Response({'message': 'Order deleted successfully'})
    

class DeliveryCenterViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = DeliveryCenter.objects.all()
    serializer_class = DeliveryCenterSerializer

class DeliveryViewSet(viewsets.ViewSet):
        permission_classes = [IsAdminUser]

        def list(self, request):
            queryset = Delivery.objects.all()
            serializer = DeliverySerializer(queryset, many=True)
            return Response(serializer.data)
        
        def create(self, request):
            data = request.data
            delivery = Delivery.objects.create(
                order_id=data['order'],
                delivery_center_id=data['delivery_center']
            )
            serializer = DeliverySerializer(delivery)
            return Response(serializer.data)
        
        def retrieve(self, request, pk=None):
            queryset = Delivery.objects.all()
            delivery = get_object_or_404(queryset, pk=pk)
            serializer = DeliverySerializer(delivery)
            return Response(serializer.data)
        
        def update(self, request, pk=None):
            delivery = Delivery.objects.get(pk=pk)
            data = request.data
            delivery.order_id = data['order']
            delivery.delivery_center_id = data['delivery_center']
            delivery.save()
            serializer = DeliverySerializer(delivery)
            return Response(serializer.data)
        
        def destroy(self, request, pk=None):
            delivery = Delivery.objects.get(pk=pk)
            delivery.delete()
            return Response({'message': 'Delivery deleted successfully'})

