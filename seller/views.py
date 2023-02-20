from django.shortcuts import render

from common.models import Seller
from seller.models import Product

# Create your views here.
def seller(request):
    return render (request, 'seller_temp/seller_login.html')

def seller_home(request):
    seller_data = Seller.objects.get(id=request.session['seller'])

    return render (request ,"seller_temp/seller_home.html",{'data':seller_data})

def add_product(request):
    msg = ''
    if request.method == 'POST':
        prod_name = request.POST['prod_name']
        prod_id = request.POST['prod_id']
        prod_desc = request.POST['prod_desc']
        prod_stock = request.POST['prod_stock']
        prod_price = request.POST['prod_price']
        prod_image = request.FILES['prod_image']

        new_product = Product(
        seller = request.session['seller'].seller_id,
        prod_name = prod_name,
        prod_num = prod_id,
        prod_des = prod_desc,
        prod_stock = prod_stock,
        prod_price = prod_price,
        prod_image = prod_image)
        new_product.save()
        msg = "Product Added Succesfully"
    return render (request ,"seller_temp/add_product.html",{'msg':msg})


def profile(request):
    seller_data = Seller.objects.get(id=request.session['seller'])
    return render (request, 'seller_temp/profile.html',{'data':seller_data})