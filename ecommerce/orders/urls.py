from django.urls import path
from orders.views import get_all_cards, add_card, order, process_payment

app_name = 'orders'

urlpatterns = [
    path('cards/', get_all_cards, name='cards'),
    path('cards/add', add_card, name='add_card'),
    path('order/', order, name='order'),
    path('orders/<int:order_id>/process/', process_payment, name='process')
]
