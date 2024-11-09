from django.shortcuts import render
from .forms import ProductForm
from .models import Product

# Create your views here.


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'product.html', {'form': form})
    else:
        form = ProductForm()
    return render(request, 'product.html', {'form': form})


def view_products(request):
    products = Product.objects.all()
    return render(request, 'view_products.html', {'products': products})
