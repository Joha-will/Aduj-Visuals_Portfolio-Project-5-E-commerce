from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from . models import Product, Category
from store_management.models import Comment


def all_products(request):
    """ A view that displays all product to customers"""
    products = Product.objects.all()
    query = None
    categories = None
    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__category_name__in=categories)
            categories = Category.objects.filter(category_name__in=categories)

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
        'current_categories': categories,
    }
    return render(request, "products/products.html", context)


def product_detail(request, product_id):
    """ A view that displays products individually"""
    product = get_object_or_404(Product, pk=product_id)
    comments = Comment.objects.filter(product=product, approved=True)

    context = {
        'product': product,
        'comments': comments,
    }
    return render(request, "products/product_detail.html", context)
