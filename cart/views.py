from django.shortcuts import render,redirect
from .models import Products,Cart
from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
# Create your views here.

def shop(request):
    product = Products.objects.all()
    return render(request, 'product-page.html', {'data': product})


def add_to_cart(request,slug):
    product = Products.objects.get(id=slug)
    cart = Cart.objects.create(product=product,quantity=1,price=product.price)
    return redirect('dashboard')

def cart(request):
    cart = Cart.objects.all()
    return render(request, 'cart.html', {'data': cart})

def delete(request,slug):
    cart = Cart.objects.get(id=slug)
    cart.delete()
    return redirect('cart')

# detail
def detail(request,slug):
    cart = Cart.objects.get(id=slug)
    print(cart.product.price)
    return render(request, 'detail.html', {'data': cart})


def checkout(request):
    # product = Products.objects.all()
    cart = Cart.objects.all()

    send_mail(
        'Your Order',
        'Thank you for your order',
        '',
        [''],
        fail_silently=False,
        html_message=render_to_string('checkout.html', {'data': cart})
    )
    return render(request, 'checkout.html')
    
