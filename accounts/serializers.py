from rest_framework import serializers
from .models import Account
from carts.serializers import CartDetailSerializer


class AccountCartSerializer(serializers.ModelSerializer):
    user_carts = CartDetailSerializer(read_only=True)

    class Meta:
        model = Account
        fields = ['id', 'name', 'user_carts']