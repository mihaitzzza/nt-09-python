from django.shortcuts import render
from products.models import Product
from helpers.cart import get_total_price


def get_cart(request):
    cart_product_ids = request.session.get('cart', {}).keys()
    products = Product.objects.filter(id__in=cart_product_ids).all()
    total_price = get_total_price(request.session.get('cart', {}), products)

    return render(request, 'products/cart.html', {
        'products': products,
        'total_price': total_price,
    })
