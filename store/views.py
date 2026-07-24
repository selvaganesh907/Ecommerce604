from django.shortcuts import render
from .models import Product

def home(request):
    products = Product.objects.all()
    return render(request,"store/home.html",{"products":products})

def vendor(request):
    return render(request,"store/vendor.html")

def customer(request):
    return render(request,"store/customer.html")

def product_upload(request):
    return render(request,"store/product_upload.html")

def cart(request):
    return render(request,"store/cart.html")

def checkout(request):
    return render(request,"store/checkout.html")