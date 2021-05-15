""" Order views. """

# Django REST Framework
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

# Permissions
from rest_framework.permissions import IsAuthenticated

# Serializers
from orders.serializers import OrderModelSerializer, CreateOrderSerializer

# Models
from orders.models import Order

class OrderViewSet(mixins.ListModelMixin,mixins.CreateModelMixin,GenericViewSet):
    """ Orders view set. """
    # serializer_class = OrderModelSerializer 
    queryset = Order.objects.all()

    def get_permissions(self):
        permissions = [IsAuthenticated]
        return [p() for p in permissions]

    def get_serializer_class(self):
        if self.action == "create":
            return CreateOrderSerializer

        return OrderModelSerializer

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        order = serializer.save()
        data = OrderModelSerializer(order).data
        return Response(data, status=status.HTTP_201_CREATED)


