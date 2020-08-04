from django.shortcuts import render
from rest_framework.generics import ListAPIView, \
    RetrieveAPIView, \
    CreateAPIView, \
    DestroyAPIView, \
    UpdateAPIView
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


class ProductDetail(RetrieveAPIView):
    queryset = queryset_product
    serializer_class = ProductDetailSerializer


class ProductCreate(CreateAPIView):
    queryset = queryset_product
    serializer_class = ProductCreateSerializer


class ProductUpdate(UpdateAPIView):
    queryset = queryset_product
    serializer_class = ProductCreateSerializer


class ProductDelete(DestroyAPIView):
    queryset = queryset_product
    serializer_class = ProductDetailSerializer


# Category
class CategoryDetail(RetrieveAPIView):
    queryset = queryset_category
    serializer_class = CategoryDetailSerializer


class CategoryCreate(CreateAPIView):
    queryset = queryset_category
    serializer_class = CategoryDetailSerializer


class CategoryDelete(DestroyAPIView):
    queryset = queryset_category
    serializer_class = CategoryDetailSerializer


class CategoryUpdate(UpdateAPIView):
    queryset = queryset_category
    serializer_class = CategoryDetailSerializer


# Comments
class CommentCreate(CreateAPIView):
    queryset = queryset_comments
    serializer_class = CommentCreateUpdateSerializer


class CommentUpdate(UpdateAPIView):
    queryset = queryset_comments
    serializer_class = CommentCreateUpdateSerializer
