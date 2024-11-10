from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductForm
from .models import Product

# View for adding a new product


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_products')
    else:
        form = ProductForm()
    return render(request, 'product.html', {'form': form})

# View for listing all products


def view_products(request):
    products = Product.objects.all()
    return render(request, 'view_products.html', {'products': products})

# View for updating an existing product


def update_product(request, id):
    product = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('view_products')
    return render(request, 'edit_product.html', {'form': form, 'product': product})

# View for deleting a product


def delete_product(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    return redirect('view_products')
