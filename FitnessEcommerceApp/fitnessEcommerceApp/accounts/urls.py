from django.urls import path
from fitnessEcommerceApp.accounts import views

urlpatterns = [
    path('login/', views.login_page, name='login')
]