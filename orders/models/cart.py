""" Cart model. """

# Django
from django.db import models

class Cart(models.Model):
    """ Cart model. """
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}'s cart"

class CartItem(models.Model):
    """ Cart item model. """
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE)
    cart = models.ForeignKey("orders.Cart", on_delete=models.CASCADE, related_name="items")
    quantity = models.IntegerField(default=1)


