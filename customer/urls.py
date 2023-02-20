from . import views
from django.urls import path


app_name = 'customer'

urlpatterns = [
    path('',views.home,name='home'),
    path('customer_signup/',views.customer,name='customer_signup'),
    path('customer_login/',views.customer_login,name='customer_login'),
    path('products/', views.products,name = 'products'),
    path('change_pass/', views.change_pass, name = 'change_pass'),
    path('profile/', views.profile, name = 'profile'),
    path('cart/', views.cart, name = 'cart'),
    path('orders/', views.orders, name = 'orders'),
]