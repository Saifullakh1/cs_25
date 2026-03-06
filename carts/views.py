from rest_framework import generics
from .models import Cart
from .serializers import CartSerializer, CartDetailSerializer


class CartAPIView(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

