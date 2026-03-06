from rest_framework import serializers
from .models import Cart
from products.models import Product
from products.serializers import ProductSerializer


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'


class CartDetailSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True)
    total = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['id', 'product', 'total']

    def get_total(self, obj):
        total = 0
        products = Product.objects.filter(product_carts=obj.id)
        for product in products:
            total += product.price
        return total

