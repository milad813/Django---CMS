from django.shortcuts import render, get_object_or_404

from shop.forms import AddProductForm
from .models import Product

# Create your views here.


def shop_home(request):
    products = Product.objects.all()
    return render(request, 'shop/shop_home.html', {'products': products})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'shop/product_detail.html', {'product': product})


def add_product(request):
    if request.method == 'POST':
        form = AddProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'shop/add_product.html', {'form': form, "msg": "Product added successfully"})
        else:
            return render(request, 'shop/add_product.html', {'form': form, 'msg': "Product not added"})
    form = AddProductForm()
    return render(request, 'shop/add_product.html', {'form': form})


def edit_product(request, pk):
    if request.method == 'POST':
        instance=get_object_or_404(Product,pk=pk)
        form = AddProductForm(request.POST,instance=instance)
        if form.is_valid():
            form.save()
            return render(request, 'shop/edit_product.html', {'form': form, "msg": "Product updated successfully"})
    product = get_object_or_404(Product, pk=pk)
    form = AddProductForm(instance=product)
    return render(request, 'shop/edit_product.html', {'form': form, 'product': product})
