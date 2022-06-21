from django.db import models
from django.conf import settings
from django.templatetags.static import static
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import gettext_lazy as _


class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='likes')  # user.likes
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        related_name='likes',
    )  # content_type.likes
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


class Category(models.Model):
    class Meta:
        verbose_name_plural = _('categories')
        ordering = ('-id',)

    name = models.CharField(max_length=128, unique=True, null=False, blank=False)

    def __str__(self):
        return f'{self.name} ({self.id})'


class Store(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='stores')
    name = models.CharField(max_length=128, unique=True, null=False, blank=False)
    logo = models.ImageField(upload_to='stores/', null=True, default=None)
    likes = GenericRelation(Like)

    def __str__(self):
        return f'{self.name} ({self.id})'


class Product(models.Model):
    class Meta:
        ordering = ('name',)

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        default=None,
        related_name='products'
    )  # category.products
    store = models.ForeignKey(
        Store,
        on_delete=models.CASCADE,
        related_name='products'
    )  # store.products
    name = models.CharField(max_length=255, unique=True)
    normal_price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0.00
    )  # 999999,99
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0.00
    )  # 999999,99
    processor_owner = models.CharField(max_length=255)
    cores_number = models.IntegerField(default=1)
    processor_technology = models.IntegerField(default=None, null=True)
    memory_capacity = models.IntegerField(default=None, null=True)
    memory_type = models.CharField(max_length=255, default=None, null=True)
    hdd_type = models.CharField(max_length=255, default=None, null=True)
    weight = models.DecimalField(max_digits=8, decimal_places=2, default=None, null=True)
    stock = models.IntegerField(default=0)
    image = models.ImageField(upload_to='products/', default=None, null=True)
    likes = GenericRelation(Like)

    @property
    def image_url(self):
        if self.image:
            return self.image.url

        return static('images/defaultProductImage.png')

    def __str__(self):
        return f'{self.name} ({self.id})'

