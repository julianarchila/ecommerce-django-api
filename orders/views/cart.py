""" Cart views. """

# Django REST Framework
from orders.serializers.cart import CartItemModelSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

# Permissions
from rest_framework.permissions import IsAuthenticated

# Serializers
from orders.serializers import CartModelSerializer, AddCartItemSerializer

# Models
from orders.models import Cart
from orders.models import CartItem


class CartViewSet(
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    GenericViewSet):
    """ Cart viewset. """
    serializer_class = CartModelSerializer

    def get_queryset(self):
        if self.action == "list":
            queryset = Cart.objects.get(user=self.request.user)
        else:
            queryset =  CartItem.objects.all()
        return queryset

    def get_serializer_class(self):
        if self.action == "list":
            serializer_class = CartModelSerializer
        else:
            serializer_class = CartItemModelSerializer

        return serializer_class



    def get_permissions(self):
        permissions = [IsAuthenticated]
        return [p() for p in permissions]


    def list(self, request, *args, **kwargs):
        """ List items in user's cart. """
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset)
        return Response(serializer.data)


    # @action(detail=False, methods=["POST"])
    def create(self, request, *args, **kwargs):
        """ Add item to the cart. """
        serializer = AddCartItemSerializer(
            data=request.data,
            context=self.get_serializer_context()
        )
        serializer.is_valid(raise_exception=True)
        cart = serializer.save()
        data = CartModelSerializer(cart).data
        return Response(data, status=status.HTTP_201_CREATED)