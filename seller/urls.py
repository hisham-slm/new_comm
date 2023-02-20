from . import views
from django.urls import path


app_name = 'seller'

urlpatterns = [
    path('seller_home/',views.seller_home,name='seller_home'),
    path('add_product/',views.add_product,name='add_product'),
    path('profile/',views.profile,name='profile'),
    path('prod_cat/',views.prod_cat,name='prod_cat'),




]