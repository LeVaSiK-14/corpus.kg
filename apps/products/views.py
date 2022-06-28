from rest_framework import viewsets
from rest_framework import filters as rest_filter
from django_filters import rest_framework as filters
from apps.products.serializers import(
    ProductSerializer, CategorySerializer,
    SubcategorySerializer, SetSerializer,
    FabricSerializer, ColorsSerializer,
    ProductCreateSerializer, CategoryListSerializer,
)
from apps.products.models import (
    Product, Category, Subcategory,
    Set, Fabric, Colors,
)
from core.paginations import CustomPagination


class CategoryModelViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    def get_serializer_class(self):
        if self.action == "retrieve":
            return CategorySerializer
        return CategoryListSerializer


class ProductModelViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    filter_backends = (filters.DjangoFilterBackend, rest_filter.SearchFilter)
    pagination_class = CustomPagination
    filterset_fields = ('hit', 'subcategory', 'prod_set', 'price', 'fabric', 'is_new')
    search_fields = ['name', ]
    
    def get_serializer_class(self):
        if self.action == 'create':
            return ProductCreateSerializer
        return ProductSerializer
    
    
class SubCategoryModelViewSet(viewsets.ModelViewSet):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ("category",)
    
    
class SetModelViewSet(viewsets.ModelViewSet):
    queryset = Set.objects.all()
    serializer_class = SetSerializer
    
    
class ColorModelViewSet(viewsets.ModelViewSet):
    queryset = Colors.objects.all()
    serializer_class = ColorsSerializer
    
    
class FabricModelViewSet(viewsets.ModelViewSet):
    queryset = Fabric.objects.all()
    serializer_class = FabricSerializer
