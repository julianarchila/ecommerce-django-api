""" Categories model. """

# Django
from django.db import models

class Category(models.Model):
    """Product category model. """
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name