from django.shortcuts import render,redirect
from django.db.models import F
from common.models import Customer
from customer.models import Cart
from seller.models import Product
from . decorators import auth_customer

# Create your views here.
def customer(request):
    return render (request, 'customer_temp\customer_signup.html')

def customer_login(request):
    return render (request, "customer_temp/customer_login.html")

@auth_customer
def products(request):
    return render (request, "customer_temp/products.html")

def change_pass(request):
    return render (request , 'customer_temp/change_pass.html')

def home(request):
    prod_list = Product.objects.all()
    return render (request, 'customer_temp\customer_home.html',{'prod_data':prod_list})
@auth_customer
def profile(request):
    customer_data = Customer.objects.get(id=request.session['customer'])
    return render (request, 'customer_temp\profile.html',{'c_data':customer_data})
@auth_customer
def cart(request):
    cart_data = Cart.objects.filter(customer_id=request.session['customer']).annotate(total = F('product__prod_price')*F('quantity'))
    # cart_data = Cart.objects.annotate(total = F('product__prod_price')*F('quantity'))
    grand_total = 0
    for products in cart_data:
        grand_total = products.total + grand_total
    request.session['grand_total'] = grand_total

    context = {
        'cart_data': cart_data,
        'grand_total' : grand_total
    }

    return render (request, 'customer_temp\cart.html',context)

@auth_customer
def orders(request):
    return render (request, 'customer_temp\order.html')
def logout(request):
    del request.session['customer']
    request.session.flush()
    return redirect('common:home')

def edit_profile(request):
    if request.method == "POST":

        name = request.POST['update_name']
        mail = request.POST['update_mail']
        address = request.POST['update_address']
        ph_num = request.POST['update_num']

        customer_data = Customer.objects.get(id=request.session['customer'])
        customer_data.customer_name = name
        customer_data.e_mail = mail
        customer_data.address = address
        customer_data.ph_number = ph_num
        
        customer_data.save()
        return redirect('customer:profile')
    cust_data = Customer.objects.get(id=request.session['customer'])
    return render(request,'customer_temp/edit_profile.html',{'customer_data':cust_data})

def product_details(request,pid):
    msg = ''
    product = Product.objects.get(id=pid)
    if request.method == 'POST':
        quantity = request.POST['qty']
        prod_exist = Cart.objects.filter(product = pid,customer = request.session['customer']).exists()
        if not prod_exist :
            item = Cart(customer_id = request.session['customer'],product_id = pid,quantity = quantity)
            item.save()
            return redirect('customer:cart')
        else:  
            msg = 'Item already added'
            
    context = {
        'product_details':product,
        'msg':msg
    }
    return render (request, 'customer_temp\product_details.html',context)

def delete_item(request,pid):
    cart_item = Cart.objects.get(product = pid, customer = request.session['customer'])
    cart_item.delete()
    return redirect ('customer:cart')
