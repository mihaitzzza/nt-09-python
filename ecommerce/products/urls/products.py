from django.urls import path
from products.views.products import get_all_products, get_product

app_name = 'products'

urlpatterns = [
    path('', get_all_products, name='all_products'),
    path('<int:product_id>/', get_product, name='product_details'),
]
