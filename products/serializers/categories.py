""" Categories serializers. """

# Django REST Framework
from rest_framework import serializers

# Model
from products.models import Category

class CategoryModelSerializer(serializers.ModelSerializer):
    """ Category model serializer. """
    class Meta:
        model = Category
        fields = ("id", "name")