from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from fitnessEcommerceApp.accounts.forms import AppUserCreationForm, AppUserLoginForm

UserModel = get_user_model()


class Login(LoginView):
    template_name = 'accounts/login.html'
    form_class = AppUserLoginForm


class Register(CreateView):
    model = UserModel
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('login')
    form_class = AppUserCreationForm

