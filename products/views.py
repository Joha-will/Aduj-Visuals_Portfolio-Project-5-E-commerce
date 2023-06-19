from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from . models import Product, Category


def all_products(request):
    """ A view that displays all product to customers"""
    products = Product.objects.all()
    query = None
    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You did not enter anything to\
                     search!")
                return redirect(reverse('products'))
            queries = Q(name__icontains=query) | Q(
                    description__icontains=query)
            products = products.filter(queries)
    context = {
        'products': products,
        'search_term': query,
    }
    return render(request, "products/products.html", context)


def all_categories(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return context


def product_detail(request, product_id):
    """ A view that displays products individually"""
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }
    return render(request, "products/product_detail.html", context)
