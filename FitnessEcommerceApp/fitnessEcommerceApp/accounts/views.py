from django.shortcuts import render


# Create your views here.
def login_page(request):
    return render(request, template_name='accounts/login.html')