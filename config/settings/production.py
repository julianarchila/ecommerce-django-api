from .base import *

SECRET_KEY = env('DJANGO_SECRET_KEY', default='s&2a&ig%3=y3&c4#%!pffr3)&k_-e72$tsv)_opghj5(@bo40m')

DEBUG = False 

ALLOWED_HOSTS = env.list("ALLOWED_HOST")

# This is going to change to a postgres database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'production.sqlite3',
    }
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # Add whitenoise middleware
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # Cors middleware
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Media

DEFAULT_FILE_STORAGE = 'storages.backends.azure_storage.AzureStorage'
STATICFILES_STORAGE = 'custom_storage.custom_azure.PublicAzureStorage'


AZURE_ACCOUNT_NAME = 'ecommercedjangostorage'
AZURE_CONTAINER = 'media'
AZURE_ACCOUNT_KEY =env.str("AZURE_ACCOUNT_KEY") 

# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
# STATIC_ROOT = BASE_DIR / "static"


CORS_ALLOWED_ORIGINS = env.list("CORS_ALLOWED_ORIGINS", default="") 