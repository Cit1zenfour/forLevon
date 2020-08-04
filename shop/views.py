from django.shortcuts import render
from rest_framework.generics import ListAPIView, \
    CreateAPIView, \
    RetrieveUpdateDestroyAPIView
from .models import Product, Category, Comment
from .serializers import \
    ProductListSerializer, \
    ProductDetailSerializer, \
    CategoryDetailSerializer, \
    ProductCreateSerializer, \
    CommentCreateUpdateSerializer

queryset_product = Product.objects.all()
queryset_category = Category.objects.all()
queryset_comments = Comment.objects.all()


# Products
class ProductList(ListAPIView):
    queryset = queryset_product
    serializer_class = ProductListSerializer


class ProductDetail(RetrieveUpdateDestroyAPIView):
    queryset = queryset_product
    serializer_class = ProductDetailSerializer


class ProductCreate(CreateAPIView):
    queryset = queryset_product
    serializer_class = ProductCreateSerializer


# Category
class CategoryDetail(RetrieveUpdateDestroyAPIView):
    queryset = queryset_category
    serializer_class = CategoryDetailSerializer


class CategoryCreate(CreateAPIView):
    queryset = queryset_category
    serializer_class = CategoryDetailSerializer


# Comments
class CommentDetail(RetrieveUpdateDestroyAPIView):
    queryset = queryset_comments


class CommentCreate(CreateAPIView):
    queryset = queryset_comments
    serializer_class = CommentCreateUpdateSerializer
