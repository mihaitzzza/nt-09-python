import stripe
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.conf import settings
from orders.models import StripeCustomer

AuthUser = get_user_model()


class Command(BaseCommand):
    def handle(self, *args, **options):
        users = AuthUser.objects.filter(stripe_customer=None)

        for user in users:
            stripe_customer = stripe.Customer.create(
                email=user.email,
                name=f'{user.first_name} {user.last_name}',
                api_key=settings.STRIPE_SECRET_KEY
            )

            StripeCustomer.objects.create(
                user=user,
                stripe_id=stripe_customer['id']
            )
