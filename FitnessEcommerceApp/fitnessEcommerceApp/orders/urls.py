
from django.urls import path

from fitnessEcommerceApp.orders.views import CartView, remove_product, create_order, CompletedOrder, update_cart

urlpatterns = [
    path('info/', CartView.as_view(), name='cart'),
    path('delete-product/<int:pk>/', remove_product, name='delete-product-cart'),
    path('create-order/<int:pk>/', create_order, name='create-order'),
    path('complete-order', CompletedOrder.as_view(), name='complete-order'),
    path('update-cart/<int:pk>', update_cart, name='update-cart')
]