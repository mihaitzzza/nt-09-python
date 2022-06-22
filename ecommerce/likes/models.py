from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType


class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='likes')  # user.likes
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        related_name='likes',
    )  # content_type.likes
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


class LikeableModel(models.Model):
    class Meta:
        abstract = True

    likes = GenericRelation(Like)
