from django.urls import path
from products.views.categories import get_all_categories

app_name = 'stores'

urlpatterns = [
    path('', get_all_categories, name='all_stores'),
]
