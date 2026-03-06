from rest_framework import generics
from .models import Account
from .serializers import AccountCartSerializer


class AccountCartAPIView(generics.RetrieveAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountCartSerializer