""" Order serializers. """

# Django REST Framework
from django.db.models import fields
from rest_framework import serializers

# Serializers
from users.serializers import UserModelSerializer
from products.serializers import ProductModelSerializer

# Models
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
