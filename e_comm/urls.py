from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/',include('ecomm_admin.urls')),
    path('',include('common.urls')),
    path('customer/',include('customer.urls')),
    path('seller/',include('seller.urls')),


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

