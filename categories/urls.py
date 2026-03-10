from django.urls import path
from .views import CategoryAPIView, CategoryRetrieveAPIView


urlpatterns = [
    path('', CategoryAPIView.as_view(), name="list"),
    path('<int:pk>', CategoryRetrieveAPIView.as_view(), name='category-retrieve')
]