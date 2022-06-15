from django.shortcuts import render
from products.models import Product


def get_cart(request):
    cart_product_ids = request.session.get('cart', {}).keys()
    products = Product.objects.filter(id__in=cart_product_ids).all()

    return render(request, 'products/cart.html', {
        'products': products
    })
