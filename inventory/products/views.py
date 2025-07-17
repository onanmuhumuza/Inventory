from django.shortcuts import render, redirect
from products.models import Product
from .forms import ProductForm
# Create your views here.
def index(requests):
    products=  Product.objects.all()
    
    return render(requests, "products/index.html",{'products': products})





def product_list_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ProductForm()

    products = Product.objects.all()
    return render(request, 'products/index.html', {'products': products, 'form': form})