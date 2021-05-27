""" Rating serializers. """


# Django REST Framework
from rest_framework import serializers

# Models
from products.models import ProductRating, Product


class RateProductSerailizer(serializers.ModelSerializer):
    """ Rate product serializer. """
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = ProductRating
        fields = "__all__"

    def validate(self, data):
        """ Check user has not already rated the product. """
        user = data.get('user')
        product = data.get('product')

        if ProductRating.objects.filter(user=user, product=product).exists():
            raise serializers.ValidationError(
                "You can't rate a product twice.")

        return data

    def create(self, data):
        rating = super().create(data)
        product = rating.product

        prom = sum(ProductRating.objects.filter(product=product).values_list(
            "stars", flat=True)) / ProductRating.objects.filter(product=product).count()
        product.rating = prom
        product.save()
        return product
