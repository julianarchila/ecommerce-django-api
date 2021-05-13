""" Product views. """

# Django REST Framework
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin

# Serializers
from products.serializers import ProductModelSerializer

# Models
from products.models import Product



class ProductViewSet(ListModelMixin,GenericViewSet):
    """Product view set. """
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer