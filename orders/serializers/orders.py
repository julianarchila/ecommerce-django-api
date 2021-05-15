""" Order serializers. """

# Django REST Framework
from django.db.models import fields
from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault

# Serializers
from users.serializers import UserModelSerializer
from products.serializers import ProductModelSerializer

# Models
from products.models import Product
from orders.models import Order, OrderItem


class OrderItemModelSerailzer(serializers.ModelSerializer):
    """ Order item model serializer. """
    product = ProductModelSerializer(read_only=True)
    class Meta:
        model = OrderItem
        exclude = ["order"]

class OrderModelSerializer(serializers.ModelSerializer):
    """ Order model serializer. """
    user = UserModelSerializer(read_only=True)
    items = OrderItemModelSerailzer(read_only=True, many=True)
    class Meta:
        model = Order 
        fields = "__all__"


class CreateOrderItemSerializer(serializers.ModelSerializer):
    """ Create order item serializer. 
    Serializer used to recive order imtes data in create order serializer.
    """
    class Meta:
        model = OrderItem
        fields = (
            "product",
            "price",
            "quantity"
        )


class CreateOrderSerializer(serializers.ModelSerializer):
    """ Create order serializer. 
    Handles OrderItems creations and Order creation.
    """
    items = CreateOrderItemSerializer(many=True)
    user = serializers.HiddenField(default=CurrentUserDefault())
    # user = serializers.CurrentUserDefault()
    class Meta:
        model = Order
        # exclude = []
        fields = "__all__"

    # def validate_items(self, data):
    #     """ Handles order items validation and creation. """
    #     for item in data:
    #         try:
    #             product = Product.objects.get(item.product)
    #         except Product.DoesNotExist:
    #             raise serializers.ValidationError(f"Product with id of {item.product} does not exist.")

    #     return data

    def create(self, data):
        """ Handles order creation. """
        items_data = data.pop("items")
        order = Order.objects.create(**data)

        for item in items_data:
            OrderItem.objects.create(**item, order=order)

        return order
        

        