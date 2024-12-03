from django.urls import path, include
from fitnessEcommerceApp.products import views

urlpatterns = [
    path('', views.ProductsView.as_view(), name='all-products'),
    path('add-to-cart/<int:pk>/', views.AddProductToCart.as_view(), name='add-product-to-cart'),
    path('add-product', views.AddProduct.as_view(), name='add-product'),
    path('<int:pk>/', include([
        path('product/', views.ProductInformation.as_view(), name='product-info'),
        path('edit/', views.EditProduct.as_view(), name='edit-product'),
        path('delete/', views.DeleteProduct.as_view(), name='delete-product')
    ]))
]