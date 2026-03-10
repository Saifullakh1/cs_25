from rest_framework import serializers
from .models import Category
from products.serializers import ProductForCategorySerializer


class CategorySerializer(serializers.ModelSerializer):
    absolute_url = serializers.HyperlinkedIdentityField(view_name="category-retrieve")
    class Meta:
        model = Category
        fields = ("id", "title", "image", "absolute_url")


class CategoryDetailSerializer(serializers.ModelSerializer):
    product_category = ProductForCategorySerializer(many=True)

    class Meta:
        model = Category
        fields = ("id", "title", "image", "product_category")