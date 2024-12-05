from django.contrib import admin

from fitnessEcommerceApp.orders.models import Order, Cart, CartItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'is_sent')
    search_fields = ('user__email',)
    list_filter = ('is_sent', 'created_at')
    ordering = ('-created_at',)


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user__email',)
    list_filter = ('user',)


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity')
    search_fields = ('cart__user__email', 'product__name')
    list_filter = ('product',)
