from django.shortcuts import render,redirect

from common.models import Customer
from seller.models import Product

# Create your views here.
def customer(request):
    return render (request, 'customer_temp\customer_signup.html')

def customer_login(request):
    return render (request, "customer_temp/customer_login.html")

def products(request):
    return render (request, "customer_temp/products.html")

def change_pass(request):
    return render (request , 'customer_temp/change_pass.html')

def home(request):
    prod_list = Product.objects.all()
    return render (request, 'customer_temp\customer_home.html',{'prod_data':prod_list})

def profile(request):
    customer_data = Customer.objects.get(id=request.session['customer'])
    return render (request, 'customer_temp\profile.html',{'c_data':customer_data})

def cart(request):
    return render (request, 'customer_temp\cart.html')

def orders(request):
    return render (request, 'customer_temp\order.html')
def logout(request):
    del request.session['customer']
    request.session.flush()
    return redirect('common:home')