from . import views
from django.urls import path


app_name = 'admin'

urlpatterns = [
    path('',views.admin_login,name='admin_login'),
    path('home/',views.admin_home,name='admin_home'),
    path('index/',views.index,name='index')
]