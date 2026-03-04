from django.urls import path
from .views import ProductAPIView, ProductRetrieveAPIView


urlpatterns = [
    path('', ProductAPIView.as_view(), name='list'),
    path('<int:pk>', ProductRetrieveAPIView.as_view(), name='retrieve')
]