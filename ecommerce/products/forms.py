from django import forms


class CartForm(forms.Form):
    quantity = forms.IntegerField(required=True, label="", initial=0, min_value=0)

    def __init__(self, *args, product=None, session=None, **kwargs):
        # if 'product' in kwargs:
        #     self._product = kwargs.pop('product')
        # else:
        #     self._product = None
        #
        # if 'session' in kwargs:
        #     self._session = kwargs.pop('session')
        # else:
        #     self._session = None
        super().__init__(*args, **kwargs)

        self._product = product
        self._session = session

    def save(self):
        # add Product with ID = <product_id> to cart in quantity = <quantity>
        quantity = self.cleaned_data['quantity']
        print('--- quantity', quantity, type(quantity))
        print('--- product', self._product)

        # if 'cart' in self._session:
        #     self._session['cart'][self._product.id] = quantity
        # else:
        #     self._session['cart'] = {
        #         self._product.id: quantity
        #     }
        if 'cart' not in self._session:
            self._session['cart'] = {}

        old_quantity = self._session['cart'].get(str(self._product.id), 0)
        self._session['cart'][self._product.id] = quantity + old_quantity
        self._session.modified = True
