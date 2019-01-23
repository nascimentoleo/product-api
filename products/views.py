from django_filters import rest_framework as filters
from rest_framework import viewsets

from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer


class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ['name']


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ['name', 'size', 'price', 'category']
