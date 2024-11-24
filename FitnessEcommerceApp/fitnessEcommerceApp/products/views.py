from django.shortcuts import render
from django.views.generic import ListView, DetailView

from fitnessEcommerceApp.products.models import Product


# Create your views here.
class ProductsView(ListView):
    template_name = 'products/products.html'
    model = Product
    context_object_name = 'products'
    paginate_by = 6


class ProductInformation(DetailView):
    template_name = 'products/product-info.html'
    model = Product
    context_object_name = 'product'

