from django.shortcuts import render
from products.models import Category


def get_all_categories(request):
    categories = Category.objects.all()

    return render(request, 'products/categories.html', {
        'categories': categories
    })
