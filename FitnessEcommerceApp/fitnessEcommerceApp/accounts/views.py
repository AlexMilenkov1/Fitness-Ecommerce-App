from django.contrib.auth import get_user_model, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView

from fitnessEcommerceApp.accounts.forms import AppUserCreationForm, AppUserLoginForm, AppProfileForm
from fitnessEcommerceApp.accounts.models import AppProfile, AppUser

UserModel = get_user_model()


class Login(LoginView):
    template_name = 'accounts/login.html'
    form_class = AppUserLoginForm


class Register(CreateView):
    model = UserModel
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('login')
    form_class = AppUserCreationForm


class ProfilePage(LoginRequiredMixin, UpdateView):
    model = AppProfile
    form_class = AppProfileForm
    template_name = 'accounts/profile-page.html'

    def get_success_url(self):
        return reverse_lazy('profile-details', kwargs={'pk': self.request.user.pk})


class ProfileDetails(LoginRequiredMixin, DetailView):
    model = AppProfile
    template_name = 'accounts/profile-details.html'
    context_object_name = 'profile'


def delete_profile(request, pk):
    profile = AppProfile.objects.get(pk=pk)
    user = AppUser.objects.get(pk=profile.pk)

    profile.delete()
    user.delete()

    logout(request)

    return redirect('index')
