from django import template
from products.models import Product

register = template.Library()


@register.filter(name='product_qty')
def get_product_qty(cart_data, product_id):
    return cart_data[str(product_id)]


# # Simple tag without using takes_context
# @register.simple_tag(name='cart_data')
# def get_cart_data(session):
#     cart_data = session.get('cart', {})
#     return len(cart_data.keys())

# Simple tag with context
@register.simple_tag(name='cart_data', takes_context=True)
def get_cart_data(context):
    cart_data = context['request'].session.get('cart', {})
    total_products = len(cart_data.keys())
    if total_products > 0:
        cart_products = Product.objects.filter(pk__in=cart_data.keys()).all()
        total_price = sum(
            [
                product.price * cart_data[str(product.id)]
                for product in cart_products
            ]
        )
    else:
        total_price = 0

    # if len(cart_products) > 0:
    #     for product in cart_products:
    #         total_price += product.price * cart_data[str(product.id)]
    # for product_id, quantity in cart_data.items():
    #     product = Product.objects.get(pk=product_id)
    #     total_price += product.price * quantity

    return {
        'total_products': total_products,
        'total_price': '%.2f' % total_price
    }


@register.inclusion_tag('products/cart_link.html', name='cart_link', takes_context=True)
def get_cart_link(context):
    cart_data = context['request'].session.get('cart', {})
    total_products = len(cart_data.keys())
    if total_products > 0:
        cart_products = Product.objects.filter(pk__in=cart_data.keys()).all()
        total_price = sum(
            [
                product.price * cart_data[str(product.id)]
                for product in cart_products
            ]
        )
    else:
        total_price = 0

    return {
        'price': '%.2f' % total_price,
        'products': total_products
    }


@register.inclusion_tag('products/like_form.html', name='like_form', takes_context=True)
def get_like_form(context, content_object, like_route):
    return {
        'path': like_route,
        'likes': len(content_object.likes.all()),
        'is_authenticated': context['request'].user.is_authenticated
    }
