from django.contrib import admin
from django.utils.html import format_html
from products.models import Product, Store


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    @admin.display(description='Image')
    def image_html(self, obj):
        return format_html(f'<img src="{obj.image_url}" width="50" />')

    list_display = ('name', 'category', 'store', 'image_html')

    def get_queryset(self, request):
        queryset = super().get_queryset(request)

        if not request.user.is_superuser:
            # user_store_ids = [store.id for store in request.user.stores.all()]
            # queryset = queryset.filter(store_id__in=user_store_ids)

            queryset = queryset.filter(store__in=request.user.stores.all())

        return queryset

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'store' and not request.user.is_superuser:
            kwargs['queryset'] = Store.objects.filter(owner=request.user)

        return super().formfield_for_foreignkey(db_field, request, **kwargs)
