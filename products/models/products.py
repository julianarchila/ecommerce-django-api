""" Product model. """

# Django
from django.db import models

class Product(models.Model):
    """ Product model. """
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=15 ,decimal_places=2)
    thumbnail = models.ImageField(upload_to="products/thumbnails/", blank=True, null=True)
    categories = models.ManyToManyField("products.category", related_name="products", blank=True)
    stock = models.PositiveIntegerField(default=1)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}: ${self.price}"



