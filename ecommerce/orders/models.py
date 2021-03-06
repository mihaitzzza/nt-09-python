from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator
from products.models import Product


class Order(models.Model):
    class StatusChoices(models.IntegerChoices):
        PENDING = 0
        COMPLETE = 1
        INCOMPLETE = 2

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, default=None)
    billing_address = models.CharField(max_length=256, null=True, default=None)
    shipping_address = models.CharField(max_length=256, null=True, default=None)
    status = models.IntegerField(choices=StatusChoices.choices, default=0, null=False)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET, null=True, default=None)
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0.00,
        validators=(MinValueValidator(0.00),)
    )  # 999999,99
    quantity = models.IntegerField(default=1, validators=(MinValueValidator(1),))


class StripeCustomer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='stripe_customer')
    stripe_id = models.CharField(max_length=256, null=False)


class StripeCard(models.Model):
    stripe_customer = models.ForeignKey(StripeCustomer, on_delete=models.CASCADE, related_name='cards')
    stripe_id = models.CharField(max_length=256, null=False)
    brand = models.CharField(max_length=20, null=True, default=None)
    last4 = models.CharField(max_length=4, null=True, default=None)
    exp_month = models.IntegerField(null=True, default=None)
    exp_year = models.IntegerField(null=True, default=None)

    def __str__(self):
        return f'**** **** **** {self.last4}'
