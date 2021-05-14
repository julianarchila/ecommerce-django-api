""" Order views. """

# Django REST Framework
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

# Permissions
from rest_framework.permissions import IsAuthenticated

# Serializers
from orders.serializers import OrderModelSerializer

# Models
from orders.models import Order

class OrderViewSet(mixins.ListModelMixin,GenericViewSet):
    """ Orders view set. """
    serializer_class = OrderModelSerializer 
    queryset = Order.objects.all()

    def get_permissions(self):
        permissions = [IsAuthenticated]
        return [p() for p in permissions]

