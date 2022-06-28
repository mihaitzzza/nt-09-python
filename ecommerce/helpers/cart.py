def get_total_price(cart_data, products):
    total_price = sum(
        [
            product.price * cart_data[str(product.id)]
            for product in products
        ]
    )

    return total_price
