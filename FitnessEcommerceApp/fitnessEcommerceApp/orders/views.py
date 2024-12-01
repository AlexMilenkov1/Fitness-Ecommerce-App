from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DeleteView, TemplateView

from fitnessEcommerceApp.orders.models import Cart, CartItem, Order


# Create your views here.
class CartView(LoginRequiredMixin, ListView):
    template_name = 'orders/shopping-cart.html'
    model = Cart

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        cart = get_object_or_404(Cart, user_id=self.request.user.id)
        cart_items = CartItem.objects.filter(cart=cart)

        total_price = sum([item.product.price * item.quantity for item in cart_items])

        context['cart_items'] = cart_items
        context['total_price'] = total_price
        context['cart'] = cart

        return context


class CompletedOrder(TemplateView):
    template_name = 'orders/completed_order.html'


def remove_product(request, pk):
    item = CartItem.objects.get(pk=pk)

    item.delete()

    return redirect('cart')


def create_order(request, pk):
    cart = Cart.objects.get(pk=pk)

    new_order = Order.objects.create(
        user=request.user,
        cart=cart
    )

    new_order.save()

    cart_items = CartItem.objects.filter(cart=cart)
    cart_items.delete()

    return redirect('complete-order')

