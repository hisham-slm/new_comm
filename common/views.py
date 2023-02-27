from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render,redirect

from common.models import Customer, Seller
from django.core.mail import send_mail


import random

# Create your views here.

def home_page(request):
    return render (request, 'home_temp\home.html')

def customer_reg(request):
    if request.method == 'POST':
        cust_name = request.POST['c_name']
        cust_gender = request.POST['c_gender']
        cust_number = request.POST['c_ph_num']
        cust_mail = request.POST['c_mail']
        cust_add = request.POST['c_add']
        cust_pass = request.POST['c_pass']
        cust_img = request.FILES['c_img']
    
        new_customer = Customer(
            customer_name = cust_name,
            gender = cust_gender,
            ph_number = cust_number,
            e_mail = cust_mail,
            address = cust_add,
            password = cust_pass,
            image = cust_img
        )
        new_customer.save()
    return render (request ,'home_temp/customer_signup.html')

def seller_reg(request):
    message = ''
    if request.method == 'POST':

        seller_name = request.POST['name']
        s_company_name = request.POST['s_company_name']
        s_account_num = request.POST['s_account_num']
        s_account_holder_name = request.POST['s_account_holder_name']
        s_ifsc = request.POST['s_ifsc']
        s_branch_name = request.POST['s_branch_name']
        s_ph_num = request.POST['s_ph_num']
        s_email = request.POST['s_email']
        s_address = request.POST['s_address']
        s_image = request.FILES['s_image']
        s_username = random.randint(1111,9999)
        s_pass = 'sel-' + seller_name.lower() + str(s_username)
        message = 'Hi Your user name is' + str(s_username) + 'and Temporary Password is ' + s_pass

        new_seller = Seller(
        seller_name = seller_name,
        company_name = s_company_name,
        acc_no = s_account_num, 
        ifsc = s_ifsc,
        branch_name = s_branch_name,
        acc_holder_name = s_account_holder_name,
        ph_num = s_ph_num,
        email = s_email,
        address = s_address,
        image = s_image,
        user_name = s_username,
        password = s_pass)
        send_mail('Username and Temporary Password',
            message,
            settings.EMAIL_HOST_USER,
            [s_email],
            fail_silently = False
        )
        new_seller.save()
    return render (request ,'home_temp/become_seller.html')


def seller_login(request):
    msg = ''
    if request.method == 'POST':
        s_username = request.POST['s_mail']
        s_pass = request.POST['s_pass']
        try:
            seller = Seller.objects.get(user_name = s_username,password = s_pass)
            request.session['seller'] = seller.id
            return redirect('seller:seller_home')

        except:
            msg = "Invalid Email or Password"
    return render (request ,'home_temp/seller_login.html',{'msg' : msg})


def customer_login(request):
    msg = ''
    if request.method == 'POST':
        cust_email = request.POST['c_mail']
        cust_pass = request.POST['c_pass']
        try:
            customer = Customer.objects.get(e_mail = cust_email,password = cust_pass)
            request.session['customer'] = customer.id
            return redirect('customer:home')
        except:
            msg = "Invalid Email ID or Password"
            

    return render (request ,'home_temp/customer_login.html',{'msg':msg})

def email_exist(request):
    email = request.POST['email']
    status = Customer.objects.filter(e_mail = email).exists()
    return JsonResponse({'status':status})