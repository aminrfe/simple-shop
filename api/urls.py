from django.urls import path, include
from rest_framework import routers
from api.views import ProductViewSet, OrderViewSet, DeliveryCenterViewSet, DeliveryViewSet

router = routers.DefaultRouter()
router.register(r'product', ProductViewSet)
router.register(r'order', OrderViewSet, basename='order')
router.register(r'delivery-center', DeliveryCenterViewSet)
router.register(r'delivery', DeliveryViewSet, basename='delivery')

urlpatterns = [
    path('', include(router.urls)),
]