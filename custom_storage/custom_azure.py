from storages.backends.azure_storage import AzureStorage

class PublicAzureStorage(AzureStorage):
    account_name = 'ecommercedjangostorage'
    account_key = 'efvytQZZ9NC31h/gCRMuDGvNrMImMIyKvc3CK82aI+NDi5hhN02+do3kOopbEUDtGLrG/8v3m7ZEEDk23H+o3A=='
    azure_container = 'static'
    expiration_secs = None