from rest_framework import serializers
from .models import Category, Product

class CategorySerializer(serializers.ModelSerializer):
    child_categories = serializers.SerializerMethodField()

    def get_child_categories(self, obj):
        child_categories = obj.child_categories.all()
        serializer = CategorySerializer(child_categories, many=True)
        return serializer.data

    class Meta:
        model = Category
        fields = ('id', 'name', 'parent_category', 'child_categories')


class ProductSerializer(serializers.ModelSerializer):
    categories = serializers.SerializerMethodField()

    def get_categories(self, obj):
        categories = obj.categories.all()
        serializer = CategorySerializer(categories, many=True)
        return serializer.data

    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'categories')

