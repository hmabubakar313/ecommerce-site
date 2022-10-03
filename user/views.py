from django.shortcuts import render
from cart.models import Products,Cart
from django.contrib.auth import logout as dj_logout
from django.contrib.auth import login as dj_login
from django.http import HttpResponse
from cart.models import Products,Cart
from django.core.mail import send_mail
# Create your views here.

def dashboard(request):
   
    product = Products.objects.all()
    return render(request, 'dashboard.html', {'data':product})

        

def login(request):
    return render(request, 'login.html')


def logout(request):
    dj_logout(request)
    # if user logged out successfully
    if not request.user.is_authenticated:
        cart = Cart.objects.all()
        cart.delete()
        return HttpResponse('Logged out')

    return HttpResponse('Not logged out')