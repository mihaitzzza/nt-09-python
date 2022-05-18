from django.urls import path, include

urlpatterns = [
    path('products/', include('products.urls.products')),
    path('stores/', include('products.urls.stores')),
]
