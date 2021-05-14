from .base import *
# from .base import env

DEBUG = env.bool("DEBUG", default=True) 

SECRET_KEY = env('DJANGO_SECRET_KEY', default='s&2a&ig%3=y3&c4#%!pffr3)&k_-e72$tsv)_opghj5(@bo40m')


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

INSTALLED_APPS += ['django_extensions'] 

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True

EMAIL_HOST_USER = env.str("EMAIL_HOST_USER") 
EMAIL_HOST_PASSWORD = env.str("EMAIL_HOST_PASSWORD")