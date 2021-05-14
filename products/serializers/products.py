""" Product serializers. """

# Django REST Framework
from rest_framework import serializers


# Model
from products.models import Product, Category

class ProductModelSerializer(serializers.ModelSerializer):
    """Product model serializer. """
    categories = serializers.StringRelatedField(many=True)
    class Meta:
        model = Product
        fields = "__all__" 

class CreateProductSerializer(serializers.ModelSerializer):
    """Create product serializer """
    categories = serializers.ListField(
        child=serializers.CharField(min_length=2, max_length=50)
    )

    class Meta:
        model = Product
        fields = (
            "name",
            "description",
            "price",
            "categories",
            "stock",
            "thumbnail"
        )

    def validate_categories(self, data):
        """ Validate categories exists and if not
        create them. """
        categories_obj = []
        for category in data:
            try:
                category_obj = Category.objects.get(name=category.lower())
            except Category.DoesNotExist:
                category_obj = Category.objects.create(name=category.lower())

            categories_obj.append(category_obj)

        return categories_obj 

    def create(self, validated_data):
        categories = validated_data["categories"]
        validated_data.pop("categories")
        product = Product.objects.create(**validated_data)
        for catg in categories:
            product.categories.add(catg.id)
        product.save()
        return product






