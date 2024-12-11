from django.contrib.auth.views import LogoutView
from django.urls import path, include
from fitnessEcommerceApp.accounts import views
from fitnessEcommerceApp.accounts.views import ProfilePage, ProfileDetails, delete_profile

urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),
    path('register/', views.Register.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('<int:pk>/', include([
        path('profile/', ProfilePage.as_view(), name='profile'),
        path('profile-details/', ProfileDetails.as_view(), name='profile-details'),
        path('profile-delete/', delete_profile, name='delete-profile')
    ]))

]