from django.contrib import admin
from django.utils.html import format_html
from products.models import Category, Store, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    @admin.display(description='Total products')
    def products_number(self, obj):
        return obj.products.count()

    list_display = ('name', 'products_number')
    ordering = ('-name',)  # use `-name` to order descending by name


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    @admin.display(description='Owner', ordering='owner__username')
    def owner_username(self, obj):
        return obj.owner.username

    list_display = ('name', 'owner_username')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    @admin.display(description='Image')
    def image_html(self, obj):
        return format_html(f'<img src="{obj.image_url}" width="50" />')

    list_display = ('name', 'category', 'store', 'image_html')


# admin.site.register(Category, CategoryAdmin)
