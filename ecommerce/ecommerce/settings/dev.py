from ecommerce.settings.base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': config('DB_HOST', 'localhost'),
        'NAME': config('DB_NAME'),
        'PORT': config('DB_PORT', 3306),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASS'),
    }
}

# CORS_ALLOWED_ORIGINS = ['http://*', 'ftp://*']
CORS_ALLOW_ALL_ORIGINS = True
