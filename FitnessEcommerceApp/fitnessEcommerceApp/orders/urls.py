
from django.urls import path

from fitnessEcommerceApp.orders.views import CartView, remove_product, create_order, CompletedOrder

urlpatterns = [
    path('info/', CartView.as_view(), name='cart'),
    path('delete-product/<int:pk>/', remove_product, name='delete-product'),
    path('create-order/<int:pk>/', create_order, name='create-order'),
    path('complete-order', CompletedOrder.as_view(), name='complete-order')
]