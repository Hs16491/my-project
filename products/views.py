from django.shortcuts import render
from .models import Product
# Create your views here.

def product_list(request):
    return render(request, 'products/product.html')

def products_list(request):
    return render(request, 'products/products.html', {'products': Product.objects.all()})