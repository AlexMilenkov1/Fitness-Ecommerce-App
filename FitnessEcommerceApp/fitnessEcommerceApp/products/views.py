from django.shortcuts import render
from django.views.generic import ListView

from fitnessEcommerceApp.products.models import Product


# Create your views here.
class ProductsView(ListView):
    template_name = 'products.html'
    model = Product
