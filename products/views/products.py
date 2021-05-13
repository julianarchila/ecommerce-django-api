""" Product views. """

# Django REST Framework
from rest_framework import permissions
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin
from rest_framework.permissions import IsAuthenticated, IsAdminUser

# Serializers
from products.serializers import ProductModelSerializer

# Models
from products.models import Product



class ProductViewSet(ListModelMixin,GenericViewSet):
    """Product view set. """
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer
    
    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        permissions = [IsAuthenticated]
        if self.action == "list":
            permissions.append(IsAdminUser)

        return [p() for p in permissions]