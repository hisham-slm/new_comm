from django.shortcuts import render

from common.models import Customer

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
    return render (request, 'customer_temp\customer_home.html')

def profile(request):
    customer_data = Customer.objects.get(id=request.session['customer'])
    return render (request, 'customer_temp\profile.html',{'c_data':customer_data})

def cart(request):
    return render (request, 'customer_temp\cart.html')

def orders(request):
    return render (request, 'customer_temp\order.html')
