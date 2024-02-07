from django.contrib import admin
from api.models import *
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description','price')
    ordering = ('name',)
    search_fields = ('name',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity')
    ordering = ('user',)
    search_fields = ('user',)    

@admin.register(DeliveryCenter)
class DeliveryCenterAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)

@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('order', 'delivery_center', 'received_at', 'delivered_at')
    ordering = ('order',)
    search_fields = ('order',)