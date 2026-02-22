from django.shortcuts import render, get_object_or_404
from .models import Category, Product

def home(request):
    categories = Category.objects.all()
    # Assuming we want to show some featured products or just the banner
    return render(request, 'gallery/home.html', {'categories': categories})

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = category.products.all()
    categories = Category.objects.all() # For nav
    return render(request, 'gallery/category_detail.html', {
        'category': category,
        'products': products,
        'categories': categories
    })

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    categories = Category.objects.all() # For nav
    return render(request, 'gallery/product_detail.html', {
        'product': product,
        'categories': categories
    })
