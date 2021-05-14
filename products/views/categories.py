""" Categories views. """

# Django REST Framework
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import AllowAny
from rest_framework import mixins




# Serializer
from products.serializers import CategoryModelSerializer

# Model
from products.models import Category

class CategoriesViewSet(mixins.ListModelMixin,GenericViewSet):
    """ Categories view set. """
    serializer_class = CategoryModelSerializer 
    queryset = Category.objects.all()
    permission_classes = [AllowAny]