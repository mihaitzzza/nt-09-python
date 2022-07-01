import stripe
from django.shortcuts import render, Http404, redirect, reverse, get_object_or_404, HttpResponse
from django.conf import settings
from django.contrib import messages
from orders.models import StripeCard, Order
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
            order = form.save()
            card = form.cleaned_data['card']
            process_payment_route = reverse('orders:process', kwargs={'order_id': order.id})

            payment_intent = stripe.PaymentIntent.create(
                amount=int(float(total_price) * 100),
                currency='ron',
                customer=request.user.stripe_customer.stripe_id,
                payment_method=card.stripe_id,
                confirm=True,
                return_url=f'{settings.CURRENT_DOMAIN}{process_payment_route}',
                api_key=settings.STRIPE_SECRET_KEY,
            )

            next_action = payment_intent.get('next_action')

            if next_action:
                return redirect(next_action['redirect_to_url']['url'])

            return redirect()
    else:
        form = OrderForm(user=request.user, cart_data=cart_data, products=products)

    return render(request, 'orders/order.html', {
        'total_price': total_price,
        'form': form,
    })


def process_payment(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    payment_intent_id = request.GET.get('payment_intent')

    if not payment_intent_id:
        raise Http404('Invalid payment intent ID.')

    payment_intent = stripe.PaymentIntent.retrieve(
        payment_intent_id,
        api_key=settings.STRIPE_SECRET_KEY
    )

    payment_error = payment_intent['last_payment_error']
    if payment_error is None:
        order.status = Order.StatusChoices.COMPLETE
        messages.success(request, 'Payment was completed.')
    else:
        order.status = Order.StatusChoices.INCOMPLETE
        messages.error(request, 'Payment was incomplete.')

    order.save()

    return redirect(reverse('homepage'))
