from django.urls import path
from fitnessEcommerceApp.support import views

urlpatterns = [
    path('add-ticket/', views.AddTicket.as_view(), name='add-ticket')
]