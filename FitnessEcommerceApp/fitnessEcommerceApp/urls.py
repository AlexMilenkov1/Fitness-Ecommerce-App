from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('fitnessEcommerceApp.common.urls')),
    path('products/', include('fitnessEcommerceApp.products.urls')),
    path('accounts/', include('fitnessEcommerceApp.accounts.urls')),
    path('cart/', include('fitnessEcommerceApp.orders.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
