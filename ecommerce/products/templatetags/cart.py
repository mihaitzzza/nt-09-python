from django import template

register = template.Library()


@register.filter(name='product_qty')
def get_product_qty(cart_data, product_id):
    return cart_data[str(product_id)]
