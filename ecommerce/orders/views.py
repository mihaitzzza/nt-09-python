import stripe
from django.shortcuts import render, Http404, redirect, reverse
from django.conf import settings
from orders.models import StripeCard
from products.models import Product
from helpers.cart import get_total_price
from orders.forms import OrderForm


def get_all_cards(request):
    stripe_cards = StripeCard.objects.filter(stripe_customer=request.user.stripe_customer).all()

    return render(request, 'orders/cards.html', {
        'cards': stripe_cards
    })


def add_card(request):
    if request.method == 'POST':
        if 'stripe_token' not in request.POST:
            raise Http404('Stripe token not available.')

        stripe_token = request.POST['stripe_token']
        card_data = stripe.Customer.create_source(
            request.user.stripe_customer.stripe_id,
            source=stripe_token,
            api_key=settings.STRIPE_SECRET_KEY
        )

        StripeCard.objects.create(
            stripe_customer=request.user.stripe_customer,
            stripe_id=card_data['id'],
            brand=card_data['brand'],
            last4=card_data['last4'],
            exp_month=card_data['exp_month'],
            exp_year=card_data['exp_year'],
        )

        return redirect(reverse('orders:cards'))

    return render(request, 'orders/add_card.html', {
        'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY
    })


def order(request):
    if request.method != 'POST':
        raise Http404('Method not allowed!')

    cart_data = request.session.get('cart', {})
    cart_product_ids = cart_data.keys()
    products = Product.objects.filter(id__in=cart_product_ids)
    total_price = get_total_price(cart_data, products)

    is_card_available = request.POST.get('card')
    cart_data = request.session.get('cart', {})

    if is_card_available:
        form = OrderForm(request.POST, user=request.user, cart_data=cart_data, products=products)
        if form.is_valid():
            card = form.cleaned_data['card']

            print('sum to be paid', float(total_price))
            payment_intent = stripe.PaymentIntent.create(
                amount=int(float(total_price) * 100),
                currency='ron',
                customer=request.user.stripe_customer.stripe_id,
                payment_method=card.stripe_id,
                confirm=True,
                return_url='/',
                api_key=settings.STRIPE_SECRET_KEY,
            )

            next_action = payment_intent.get('next_action')
            print('--- next_action', next_action)
            # print('---', next_action['redirect_to_url'])

            if next_action:
                print("next_action['use_stripe_sdk']['stripe_js']", next_action['use_stripe_sdk']['stripe_js'])
                return redirect(next_action['use_stripe_sdk']['stripe_js'])

            # form.save()
            # return redirect()
            # pass
    else:
        form = OrderForm(user=request.user, cart_data=cart_data, products=products)

    return render(request, 'orders/order.html', {
        'total_price': total_price,
        'form': form,
    })
