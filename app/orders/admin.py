from django.contrib import admin

from app.orders.models import Order, OrderFoodUnifier

# Register your models here.

admin.site.register(Order)
admin.site.register(OrderFoodUnifier)
