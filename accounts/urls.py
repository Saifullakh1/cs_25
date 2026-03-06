from django.urls import path
from .views import AccountCartAPIView


urlpatterns = [
    path('cart/<int:pk>', AccountCartAPIView.as_view(), name='cart')
]