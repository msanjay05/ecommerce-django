from django.contrib import admin

from .models import OrderItem,ShippingAddress,Product,Customer,Order
# Register your models here.
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
admin.site.register(Customer)
admin.site.register(Product)
