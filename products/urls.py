from django.urls import path
from .views import ProductAPIView, ProductRetrieveAPIView, FavoriteAPIView


urlpatterns = [
    path('', ProductAPIView.as_view(), name='list'),
    path('<int:pk>', ProductRetrieveAPIView.as_view(), name='retrieve'),
    path('favorite/', FavoriteAPIView.as_view(), name='favorite'),
]