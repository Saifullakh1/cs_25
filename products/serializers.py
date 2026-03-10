from rest_framework import serializers
from .models import Product, Favorite


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'


class ProductForCategorySerializer(serializers.ModelSerializer):
    absolute_url = serializers.HyperlinkedIdentityField(view_name='retrieve')

    class Meta:
        model = Product
        fields = ("id", "title", "image", "price", "currency", "absolute_url")