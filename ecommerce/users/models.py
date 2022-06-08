from django.db import models
from django.conf import settings
from django.templatetags.static import static
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import BaseUserManager


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


class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, password, **kwargs):
        """
        Create and save a user with the given username, email, and password.
        """
        email = self.normalize_email(email)

        user = self.model(email=email, first_name=first_name, last_name=last_name, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, email, password, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)

        if kwargs.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if kwargs.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(first_name, last_name, email, password, **kwargs)


class AuthUser(AbstractUser):
    username = None
    first_name = models.CharField(_('first name'), max_length=150, blank=False, null=False)
    last_name = models.CharField(_('last name'), max_length=150, blank=False, null=False)
    email = models.EmailField(_('email address'), blank=False, null=False, unique=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
