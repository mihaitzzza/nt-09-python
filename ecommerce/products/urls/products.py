from django.urls import path
from products.views.products import get_all_products, get_product, add_to_cart, like_product

app_name = 'products'

urlpatterns = [
    path('', get_all_products, name='all_products'),  # /products
    path('<int:product_id>/add_to_cart', add_to_cart, name='add_to_cart'),  # /products/<product_id>
    path('<int:product_id>/', get_product, name='product_details'),  # /products/<product_id>
    # path('<int:product_id>/like/', like_product, name='like'),  # /products/<product_id>/like
]
