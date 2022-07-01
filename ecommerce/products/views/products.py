from django.shortcuts import render, Http404, get_object_or_404, redirect, reverse
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from products.models import Product
from products.forms.cart import CartForm
from products.forms.filter import SearchAndFilterForm
from likes.models import Like


def get_all_products(request):
    filter_form = SearchAndFilterForm(request.GET)
    if filter_form.is_valid():
        products = filter_form.get_results()
    else:
        raise Http404('Search and filter form is invalid!')

    paginator = Paginator(products, 6)  # use 6 products per each page.

    page = request.GET.get('page', 1)
    products_page = paginator.get_page(page)

    cart_form = CartForm()

    return render(request, 'products/products.html', {
        "products_page": products_page,
        "cart_form": cart_form,
        "filter_form": filter_form,
        "total_products": len(products)
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

        quantity = form.cleaned_data["quantity"]
        messages.success(request, f'Product {product.name} was added to cart {quantity} times.')
    else:
        messages.error(request, f'Product {product.name} was not added to cart.')

    page = request.GET.get('page')
    return redirect(f"{reverse('products:all_products')}?page={page}")  # products/?page=<page_number>


@login_required
def like_product(request, product_id):
    if request.method != 'POST':
        raise Http404('This method is not supported.')

    product = get_object_or_404(Product, pk=product_id)
    like = product.likes.filter(user=request.user).first()
    if like is None:
        Like.objects.create(
            user=request.user,
            content_object=product
        )
    else:
        like.delete()

    return redirect(reverse('products:product_details', kwargs={'product_id': product.id}))
