from django.urls import path
from products.views.stores import get_all_stores, get_store, like_store

app_name = 'stores'

urlpatterns = [
    path('', get_all_stores, name='all_stores'),
    path('<int:store_id>/', get_store, name='store_details'),
    path('<int:store_id>/like/', like_store, name='like'),
]
