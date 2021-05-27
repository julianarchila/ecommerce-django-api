""" Product views. """

# Django REST Framework
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework import mixins
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.decorators import action


# Serializers
from products.serializers import (
    ProductModelSerializer,
    CreateProductSerializer,
    RateProductSerailizer
)

# Models
from products.models import Product


class ProductViewSet(
        mixins.ListModelMixin,
        mixins.CreateModelMixin,
        mixins.UpdateModelMixin,
        mixins.RetrieveModelMixin,
        mixins.DestroyModelMixin,
        GenericViewSet):
    """Product view set. """
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        permissions = [IsAuthenticated]
        if self.action == "list":
            permissions = [AllowAny]
        elif self.action != "rate":
            permissions.append(IsAdminUser)

        return [p() for p in permissions]

    def create(self, request, *args, **kwargs):
        serializer = CreateProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        product = serializer.save()
        data = ProductModelSerializer(product).data
        return Response(data=data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=["GET"])
    def rate(self, request, *args, **kwargs):
        data = {
            "product": self.get_object().id, 
            "stars": request.query_params.get("stars")
        }
        serializer = RateProductSerailizer(data=data, context=self.get_serializer_context())
        serializer.is_valid(raise_exception=True)
        product = serializer.save()
        data = ProductModelSerializer(product).data
        return Response(data=data, status=status.HTTP_201_CREATED)
