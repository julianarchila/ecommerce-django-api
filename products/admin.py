from django.contrib import admin

# Register your models here.
from .models import Product, Category, ProductRating

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(ProductRating)
