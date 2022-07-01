from django import forms
from orders.models import Order, OrderItem
from orders.models import StripeCard


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ['user', 'status']

    card = forms.ChoiceField(
        widget=forms.RadioSelect,
        label='Card',
        choices=(),
    )

    def __init__(self, *args, **kwargs):
        self._user = kwargs.pop('user')
        self._cart_data = kwargs.pop('cart_data')
        self._products = kwargs.pop('products')

        super().__init__(*args, **kwargs)

        self.fields['card'].choices = (
            (card.id, str(card))
            for card in StripeCard.objects.filter(stripe_customer=self._user.stripe_customer).all()
        )

    def clean_card(self):
        card_id = self.cleaned_data['card']

        print('card', card_id)
        try:
            stripe_card = StripeCard.objects.get(pk=card_id, stripe_customer=self._user.stripe_customer)
        except StripeCard.DoesNotExist:
            stripe_card = None

        if not stripe_card:
            raise forms.ValidationError('Invalid card.')

        return stripe_card

    def save(self, commit=True):
        order = super().save(commit=False)
        order.user = self._user

        order_items = []
        for product in self._products:
            order_items.append(
                OrderItem(
                    order=order,
                    product=product,
                    price=product.price,
                    quantity=self._cart_data.get(str(product.id))
                )
            )

        if commit is True:
            order.save()

            for order_item in order_items:
                order_item.save()

        return order
