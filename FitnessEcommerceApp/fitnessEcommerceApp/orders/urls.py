
from django.urls import path

from fitnessEcommerceApp.orders.views import CartView

urlpatterns = [
    path('info/', CartView.as_view(), name='cart')
]