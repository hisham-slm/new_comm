from . import views
from django.urls import path


app_name = 'seller'

urlpatterns = [
    path('seller_home',views.seller_home,name='seller_home'),
    path('add_product',views.add_product,name='add_product'),
    path('profile',views.profile,name='profile'),
    path('prod_cat',views.prod_cat,name='prod_cat'),
    path('logout',views.logout,name='logout'),
    path('change_password',views.change_password,name='change_password'),
    path('update_stock',views.update_stock,name='update_stock'),




]