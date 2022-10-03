
from django.contrib import admin
from django.urls import path,include
from cart import views

urlpatterns = [
    path('', views.shop, name='shop'),
    path('add_to_cart/<slug>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
    path('delete/<slug>/', views.delete, name='delete'),
    path('detail/<slug>/', views.detail, name='detail'),
    path('checkout/', views.checkout, name='checkout'),
]
