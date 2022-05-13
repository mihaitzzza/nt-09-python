from django.urls import path
from products.views import get_all_products, get_product

urlpatterns = [
    path('', get_all_products),
    path('<int:product_id>/', get_product),
]
