from django.db import models
from django.conf import settings
from django.templatetags.static import static


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to='profile_images/', default=None, null=True)

    @property
    def image_url(self):
        if self.avatar:
            return self.avatar.url

        return static('images/userDefaultImage.png')

    def __str__(self):
        return f'{self.user.username} Profile ({self.id})'
