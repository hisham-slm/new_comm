from . import views
from django.urls import path


app_name = 'common'

urlpatterns = [
    path('',views.home_page, name='home'),
    path('customer_reg/', views.customer_reg, name = 'customer_reg'),
    path('seller_reg/', views.seller_reg, name = 'seller_reg'),
    path('customer_login/', views.customer_login, name = 'customer_login'),
    path('seller_login/', views.seller_login, name = 'seller_login'),
    path('email_exist/', views.email_exist, name = 'email_exist'),  

]