from django.shortcuts import render, Http404, get_object_or_404, redirect, reverse
from django.core.paginator import Paginator
from products.models import Product
from products.forms import CartForm


def get_all_products(request):
    products = Product.objects.order_by('-price').all()

    paginator = Paginator(products, 6)  # use 6 products per each page.

    page = request.GET.get('page', 1)
    products_page = paginator.get_page(page)

    form = CartForm()

    return render(request, 'products/products.html', {
        "products_page": products_page,
        "form": form,
    })


def get_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    return render(request, 'products/product.html', {
        "product": product
    })


def add_to_cart(request, product_id):
    if request.method == 'GET':
        raise Http404('Method not allowed.')

    product = get_object_or_404(Product, pk=product_id)

    form = CartForm(request.POST, product=product, session=request.session)

    if form.is_valid():
        form.save()

    page = request.GET.get('page')
    return redirect(f"{reverse('products:all_products')}?page={page}")  # products/?page=<page_number>

