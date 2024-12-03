from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import IntegrityError
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


def update_cart(request, pk):
    if request.method == 'POST':
        cart = get_object_or_404(Cart, pk=pk)

        quantities = request.POST.dict()

        for key, value in quantities.items():
            # Check if the key matches the pattern "quantities[<item_id>]"
            if key.startswith('quantities[') and key.endswith(']'):
                try:
                    # Extract the item ID from the key
                    item_id = key[11:-1]  # Removes "quantities[" and "]"
                    item = CartItem.objects.get(id=item_id, cart=cart)

                    item.quantity = int(value)  # Update the quantity
                    item.save()
                except (CartItem.DoesNotExist, ValueError):
                    # Handle missing CartItem or invalid quantity gracefully
                    continue
                except IntegrityError:
                    pass

        return redirect('create-order', pk=cart.id)


def create_order(request, pk):
    cart = Cart.objects.get(pk=pk)

    new_order = Order.objects.create(
        user=request.user,
        cart=cart
    )

    new_order.save()

    cart_items = CartItem.objects.filter(cart=cart)

    for item in cart_items:
        product = item.product
        quantity = item.quantity

        product.in_stock -= quantity

        product.save()

    cart_items.delete()

    return redirect('complete-order')
