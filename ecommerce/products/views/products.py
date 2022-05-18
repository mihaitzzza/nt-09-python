from django.shortcuts import render, HttpResponse, Http404

products = [
    {
        "id": index,
        "name": f"Product #{index}"
    } for index in range(1, 61)
]


# Create your views here.
def get_all_products(request):
    return render(request, 'products.html', {
        "products": products
    })


def get_product(request, product_id):
    try:
        product = [p for p in products if p["id"] == product_id][0]
    except IndexError:
        raise Http404('This product is not available.')

    return render(request, 'product.html', {
        "product": product
    })
