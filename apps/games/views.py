from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from apps.games.models import Category, Subcategory
from apps.games.serializers import CategorySerializer, SubCategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubCategoryViewSet(viewsets.ModelViewSet):
    queryset = Subcategory.objects.all()
    serializer_class = SubCategorySerializer
    pagination_class = PageNumberPagination

