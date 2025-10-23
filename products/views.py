from django.shortcuts import render
from .models import Product

def home_view(request):
    return render(request, "home.html", {"title": "Home"})

def product_list_view(request):
    products = Product.objects.all()
    return render(request, "products/list.html", {"products": products, "title": "Products"})


