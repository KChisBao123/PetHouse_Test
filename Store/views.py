from itertools import product
from django.shortcuts import render
from .models import Cartitems, Customer, Product, Cart   # new
from django.http import JsonResponse
import json

# Create your views here.
def store(request):
    products = Product.objects.all() 
    return render(request, 'store.html',{'products':products}) 
    
def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        cart, created = Cart.objects.get_or_create(customer = customer, completed = False)
        cartitems = cart.cartitems_set.all()
    else:
        cartitems = []
        cart = {"get_cart_total": 0, "get_itemtotal": 0}


    return render(request, 'cart.html', {'cartitems' : cartitems, 'cart':cart})



    
def checkout(request):
    return render(request, 'checkout.html',{})