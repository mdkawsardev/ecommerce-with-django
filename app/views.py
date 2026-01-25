from django.shortcuts import render
from .models import Product
from math import ceil
def index(request):
    products = Product.objects.all()
    n = len(products)
    nSlide = n//4 + ceil((n/4) - (n//4))
    context = {
        'products': products,
        'no_of_slides': nSlide,
        'range': range(1, nSlide)
    }
    return render(request, 'index.html', context)

a = 12//4
b = 12/4
print(a)
print(b)
print(a - b)
print(ceil(a - b))
print()
print(12//4 + ceil((12/4) - (12//4)))