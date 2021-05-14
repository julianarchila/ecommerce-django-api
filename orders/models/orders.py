""" Order model. """

# Django
from django.db import models

class Order(models.Model):
    # Model b
    """ Order model. """
    # User information
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="orders")

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    # Shping information
    address = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    place = models.CharField(max_length=100)


    # Other order information
    paid_amount = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(
        "Completed",
        default=False,
        help_text=("Set true when user get the products.")
    )

    class Meta:
        ordering = ["-created_at"]


    

class OrderItem(models.Model):
    # Model a
    """ Order Item model. """
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.product)
