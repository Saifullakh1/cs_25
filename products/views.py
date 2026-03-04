from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer


class ProductAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer