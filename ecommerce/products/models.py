from django.db import models
from django.conf import global_settings


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True, null=False, blank=False)


class Store(models.Model):
    owner = models.ForeignKey(global_settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='stores')
    name = models.CharField(max_length=128, unique=True, null=False, blank=False)
    logo = models.ImageField(upload_to='stores/', null=True, default=None)
