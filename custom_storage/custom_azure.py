from storages.backends.azure_storage import AzureStorage
from config.settings.base import env

class PublicAzureStorage(AzureStorage):
    account_name = 'ecommercedjangostorage'
    account_key = env.str("AZURE_ACCOUNT_KEY") 
    azure_container = 'static'
    expiration_secs = None