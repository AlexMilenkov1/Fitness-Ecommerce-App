from django.urls import path
from fitnessEcommerceApp.products import views

urlpatterns = [
    path('', views.ProductsView.as_view(), name='all-products'),
    path('product/<int:pk>', views.ProductInformation.as_view(), name='product-info')
]