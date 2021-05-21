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
    Serializer used to recive order items data in create order serializer.
    """
    class Meta:
        model = OrderItem
        fields = (
            "product",
            "quantity"
        )

    def validate(self, data):
        """ Asing price to current product price and creates object. """
        product =  data["product"]

        if product.stock < data["quantity"]:
            raise serializers.ValidationError("There is not enough stock")

        data["price"] = product.price
        return data


class CreateOrderSerializer(serializers.ModelSerializer):
    """ Create order serializer. 
    Handles OrderItems creations and Order creation.
    """
    items = CreateOrderItemSerializer(many=True)
    user = serializers.HiddenField(default=CurrentUserDefault())
    # user = serializers.CurrentUserDefault()
    class Meta:
        model = Order
        fields = "__all__"

            
    def create(self, data):
        """ Handles order creation. """
        items_data = data.pop("items")
        order = Order.objects.create(**data)

        for item in items_data:
            order_item = OrderItem.objects.create(**item, order=order)
            product = order_item.product
            product.stock -= order_item.quantity
            product.save()

        return order
        

        