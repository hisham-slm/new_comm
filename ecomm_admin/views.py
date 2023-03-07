from django.shortcuts import render,redirect
from ecomm_admin.models import Admin
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.


def admin_login(request):
    msg = ''
    if request.method == 'POST':
        admin_username = request.POST['username']
        admin_pass = request.POST['password']
        try:
            admin = Admin.objects.get(username = admin_username,password = admin_pass)
            request.session['admin'] = admin.id
            return redirect('admin:admin_home')
        except:
            msg = 'Invalid Username or Password'
    return render(request, 'admin_temp/admin_login.html',{'msg':msg})

def admin_home(request):
    return render (request, 'admin_temp/admin_home.html')

@api_view(['GET'])
def index(request):
    message = "Congratulations, you have created an API"
    return Response(message)

