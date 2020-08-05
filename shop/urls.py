from django.urls import path
from .api.views import *

urlpatterns = [
    path('product/', ProductList.as_view()),

    path('product/<int:pk>', ProductDetail.as_view()),
    path('product/create/', ProductCreate.as_view()),

    path('category/<int:pk>', CategoryDetail.as_view()),
    path('category/create/', CategoryCreate.as_view()),

    path('comment/<int:pk>/', CommentDetail.as_view()),
    path('comment/create/', CommentCreate.as_view()),

]
