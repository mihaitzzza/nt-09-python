from django.contrib import admin
from django.contrib.auth import get_user_model
from products.models import Store

AuthUser = get_user_model()


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    @admin.display(description='Owner', ordering='owner__username')
    def owner_username(self, obj):
        return obj.owner.username

    list_display = ('name', 'owner_username', 'logo')

    def get_list_display(self, request):
        list_display = super().get_list_display(request)

        if not request.user.is_superuser:
            list_display = list(list_display)
            list_display.remove('owner_username')

        return list_display

    def get_queryset(self, request):
        queryset = super().get_queryset(request)

        if not request.user.is_superuser:
            queryset = queryset.filter(owner=request.user)

        return queryset

    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj=obj)

        if not request.user.is_superuser:
            fields.remove('owner')

        return fields

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'owner':
            kwargs['queryset'] = AuthUser.objects.filter(is_staff=True)

        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def save_model(self, request, obj, form, change):
        if not request.user.is_superuser and obj.pk is None:
            obj.owner = request.user

        super().save_model(request, obj, form, change)
