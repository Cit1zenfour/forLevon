from rest_framework import serializers
from .models import Product, \
    Category, \
    Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    product = serializers.SlugRelatedField(slug_field='title', read_only=True)


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('title', 'created_time', 'category')

    category = serializers.SlugRelatedField(slug_field='title', read_only=True)


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    category = serializers.SlugRelatedField(slug_field='title', read_only=True)
    comments = CommentSerializer(read_only=True, many=True)


class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ('created_time',)


class CommentCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude = ('user',)
