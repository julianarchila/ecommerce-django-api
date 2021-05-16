""" Product Rating model. """

# Django
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class ProductRating(models.Model):
    """ Product rating model . """
    user = models.ForeignKey("users.User", on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE)
    stars = models.PositiveIntegerField(validators=[MaxValueValidator(5)])