from django.shortcuts import render, Http404, get_object_or_404
from products.models import Product


def get_all_products(request):
    products = Product.objects.all()

    return render(request, 'products.html', {
        "products": products
    })


def get_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    return render(request, 'product.html', {
        "product": product
    })
