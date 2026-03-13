from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class ReviewForProductSerializer(serializers.ModelSerializer):
    account_name = serializers.CharField(source='account.name')
    class Meta:
        model = Review
        fields = ['id', 'rating', 'comment', 'account_name']