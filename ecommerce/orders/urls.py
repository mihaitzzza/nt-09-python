from django.urls import path
from orders.views import get_all_cards, add_card

app_name = 'orders'

urlpatterns = [
    path('cards/', get_all_cards, name='cards'),
    path('cards/add', add_card, name='add_card'),
]
