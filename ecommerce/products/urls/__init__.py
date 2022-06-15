from django.urls import path, include
from products.views.cart import get_cart

urlpatterns = [
    path('products/', include('products.urls.products')),
    path('stores/', include('products.urls.stores')),
    path('categories/', include('products.urls.categories')),
    path('cart/', get_cart, name='cart'),
]
