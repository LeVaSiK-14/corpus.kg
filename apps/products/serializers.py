from rest_framework import serializers
from .models import (
    Category, Colors, Fabric,
    Product, Set, Subcategory,
    Stock, GoodCredit
)

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'
        

class GoodCreditSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodCredit
        fields = '__all__'


class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = ('id', 'name', 'image')
        
        
class CategorySerializer(serializers.ModelSerializer):
    sub_categories = SubcategorySerializer(read_only=True, many=True)
    class Meta:
        model = Category
        fields = ('id', 'name', 'image', 'sub_categories')
        
        
class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'image', )





class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id', 'subcategory', 'prod_set', 'name', 
            'vendor_code', 'color', 'fabric', 'price', 
            'discount', 'sale', 'hit', 'is_new', 'date_added', 
            'image', 'image2', 'image3', 'image4', 
            'image5', 'image6', "description",
        )


class SetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Set
        fields = ('id', 'name',)


class FabricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fabric
        fields = ('id', 'fabric_name',)


class ColorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colors
        fields = ('id', 'color_name',)


class ProductSerializer(serializers.ModelSerializer):
    subcategory = serializers.ReadOnlyField(source='subcategory.name')
    prod_set = serializers.ReadOnlyField(source="prod_set.name")
    color = serializers.ReadOnlyField(source="color.color_name")
    fabric = serializers.ReadOnlyField(source="fabric.fabric_name")

    class Meta:
        model = Product
        fields = (
            "id", "subcategory", "prod_set", "name",
            "vendor_code", "color", "fabric", "price",
            "discount", "sale", "hit", "is_new", "date_added",
            "image", "image2", "image3", "image4",
            "image5", "image6", "description", 
            "date_added", "discount_price", 
        )
