from django.http import JsonResponse
from django.shortcuts import render,redirect
from rest_framework.response import Response
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
        seller_id = request.session['seller'],
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

def prod_cat (request):
    prod_data = Product.objects.filter(seller_id=request.session['seller'])

    return render (request, 'seller_temp\product_catelogue.html',{'prod_data':prod_data})

def logout(request):
    del request.session['seller']
    request.session.flush()
    return redirect('common:home')




def change_password (request):
    if request.method == "POST":
        old_pass = request.POST['old_pass']
        new_pass = request.POST['new_pass']
        conf_pass = request.POST['conf_pass']

        seller = Seller.objects.get(id = request.session['seller'])
        if old_pass != seller.password:
            msg = 'Wrong pass'
            return msg
    return render (request, 'seller_temp\change_password.html',{'seller':msg})


def update_stock(request):
    if request.method == 'POST':
        user_input = request.POST['prod_name']
        try:
            prod_data = Product.objects.filter(prod_name = user_input)
            status = True
            return JsonResponse(status,prod_data,user_input)
        except:
            status = False
            msg = 'Nothing to show here'
            return JsonResponse(status,msg)

    
    return render(request, 'seller_temp/update_stock.html')
