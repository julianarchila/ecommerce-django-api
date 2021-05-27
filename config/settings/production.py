from .base import *

SECRET_KEY = env('DJANGO_SECRET_KEY')

DEBUG = False 

ALLOWED_HOSTS = ["*"] 

# This is going to change to a postgres database
import dj_database_url
DATABASES = {
    'default': dj_database_url.config(
        default=env.str("DATABASE_URL")
    ) 
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


CORS_ALLOW_ALL_ORIGINS = True