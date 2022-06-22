from django.shortcuts import render
from django.conf import settings


def get_all_cards(request):
    return render(request, 'orders/cards.html', {
        'cards': []
    })


def add_card(request):
    print('\n' * 2)
    print('--- GET', request.GET)
    print('--- POST', request.POST)
    print('\n' * 2)

    return render(request, 'orders/add_card.html', {
        'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY
    })
