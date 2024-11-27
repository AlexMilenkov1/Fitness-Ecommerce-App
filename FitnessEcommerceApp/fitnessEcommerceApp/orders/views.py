from django.shortcuts import render
from django.views.generic import CreateView

from fitnessEcommerceApp.orders.models import Cart


# Create your views here.
class CartView(CreateView):
    template_name = 'shopping-cart.html'
    model = Cart

