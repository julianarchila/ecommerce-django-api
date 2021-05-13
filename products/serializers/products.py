""" Product serializers. """

# Django REST Framework
from rest_framework import serializers


# Model
from products.models import Product

class ProductModelSerializer(serializers.ModelSerializer):
    """Product model serializer. """
    categories = serializers.StringRelatedField(many=True)
    class Meta:
        model = Product
        fields = "__all__" 
