from enum import Enum
from django import forms
from products.models import Product, Store, Category


class SearchAndFilterForm(forms.Form):
    order_by_choices = (
        ('price_asc', 'Price ascending'),
        ('price_desc', 'Price descending'),
    )

    category = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, required=False, choices=(
        (category.id, category.name)
        for category in Category.objects.all()
    ))
    name = forms.CharField(max_length=255, required=False)
    price_min = forms.IntegerField(min_value=0, required=False)
    price_max = forms.IntegerField(min_value=0, required=False)
    order_by = forms.ChoiceField(widget=forms.Select, choices=order_by_choices, required=False)
    memory_capacity = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, required=False, choices=())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        available_memory_capacity = set(product.memory_capacity for product in Product.objects.all())
        self.fields['memory_capacity'].choices = (
            (data, f'{data} GB') for data in available_memory_capacity
        )

    def get_results(self):
        name = self.cleaned_data.get('name')
        category_ids = self.cleaned_data.get('category')
        price_min = self.cleaned_data.get('price_min')
        price_max = self.cleaned_data.get('price_max')
        order_by = self.cleaned_data.get('order_by')
        memory_capacity = self.cleaned_data.get('memory_capacity')

        if order_by == 'price_asc':
            products = Product.objects.order_by('price')
        else:
            products = Product.objects.order_by('-price')

        if name:
            products = products.filter(name__icontains=name)

        if price_min:
            products = products.filter(price__gte=price_min)

        if price_max:
            products = products.filter(price__lte=price_max)

        if len(category_ids) > 0:
            products = products.filter(category__id__in=category_ids)

        if len(memory_capacity) > 0:
            products = products.filter(memory_capacity__in=memory_capacity)

        return products.all()
