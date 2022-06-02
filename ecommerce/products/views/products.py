from django.shortcuts import render, Http404, get_object_or_404
from products.models import Product


def get_all_products(request):
    products = Product.objects.order_by('-price').all()

    print('--- HTTP method:', request.method)
    if request.method == 'GET':
        print('--- GET PARAMS', request.GET)
        param_1 = request.GET.get('param1')
        print('param_1', param_1)
        param_2 = request.GET.get('param2')
        print('param_2', param_2)
        param_3 = request.GET.get('param3')
        print('param_3', param_3)

    return render(request, 'products/products.html', {
        "products": products
    })


def get_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    return render(request, 'products/product.html', {
        "product": product
    })
