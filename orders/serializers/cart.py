""" Cart serializers. """

# Django REST Framework
from rest_framework import serializers

# Model
from orders.models import Cart, CartItem

# Serializres
from products.serializers import ProductModelSerializer


class CartItemModelSerializer(serializers.ModelSerializer):
    """ Cart item model serializer. """
    product = ProductModelSerializer(read_only=True)
    class Meta:
        model = CartItem
        fields = "__all__"

class CartModelSerializer(serializers.ModelSerializer):
    """ Cart model serializer. """
    items = CartItemModelSerializer(read_only=True, many=True)
    class Meta:
        model = Cart
        exclude = ["id", "user"]

class AddCartItemSerializer(serializers.ModelSerializer):
    """ Add item to cart serializer """
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = CartItem
        fields = ("product", "quantity", "user")
        extra_kwargs = {'quantity': {'required': True}}

    def validate(self, data):
        """ Validate there is enough stock."""
        product =  data["product"]

        if product.stock < data["quantity"]:
            raise serializers.ValidationError("There is not enough stock")

        return data

    def create(self, data):
        user = data.pop("user") 
        cart = Cart.objects.get(user=user)
        cart_item = CartItem.objects.create(**data, cart=cart)
        return cart 

    
class UpdateCartItemSerializer(serializers.ModelSerializer):
    """ Update cart item serializer. """
    class Meta:
        model = CartItem
        fields = ("quantity",)

    def validate_quantity(self, quantity):
        product = self.instance.product

        if product.stock < quantity:
            raise serializers.ValidationError("There is not enough stock")

        return quantity 


    

