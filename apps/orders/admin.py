from django.contrib import admin

from apps.orders.models import Order, OrderItem


class OrderAdmin(admin.ModelAdmin):
    ...


class OrderItemAdmin(admin.ModelAdmin):
    ...


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
