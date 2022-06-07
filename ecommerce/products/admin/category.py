from django.contrib import admin
from products.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    @admin.display(description='Total products')
    def products_number(self, obj):
        return obj.products.count()

    list_display = ('name', 'products_number')
    ordering = ('-name',)  # use `-name` to order descending by name
