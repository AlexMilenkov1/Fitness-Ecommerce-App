from django.urls import path

from fitnessEcommerceApp.common.views import IndexPage

urlpatterns = [
    path('', IndexPage.as_view(), name='index')
]