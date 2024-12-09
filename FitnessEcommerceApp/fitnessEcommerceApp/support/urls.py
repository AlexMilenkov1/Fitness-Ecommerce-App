from django.urls import path
from fitnessEcommerceApp.support import views

urlpatterns = [
    path('add-ticket/', views.AddTicket.as_view(), name='add-ticket'),
    path('tickets/', views.TicketsForReview.as_view(), name='review-tickets'),
    path('resolve-ticket/<int:pk>', views.resolve_ticket, name='resolve-ticket')
]