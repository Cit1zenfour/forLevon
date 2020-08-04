from django.urls import path, include
from .views import *



urlpatterns = [
    path('product/', ProductList.as_view()),
    path('product/<int:pk>', ProductDetail.as_view()),
    path('product/create/', ProductCreate.as_view()),
    path('product/update/', ProductUpdate.as_view()),
    path('product/delete/<int:pk>/', ProductDelete.as_view()),

    path('category/<int:pk>', CategoryDetail.as_view()),
    path('category/create/', CategoryCreate.as_view()),
    path('category/update/', CategoryUpdate.as_view()),
    path('category/delete/<int:pk>', CategoryDelete.as_view()),

    path('comment/create/', CommentCreate.as_view()),
    path('comment/update/', CommentUpdate.as_view()),

]





