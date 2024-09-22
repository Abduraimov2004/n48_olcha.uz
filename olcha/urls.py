from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('categories/', CategoryListApiView.as_view(), name='categories'),
    path('groups/', GroupListApiView.as_view(), name='groups'),
    path('category/<slug:slug>/',CategoryDetail.as_view(), name='category'),
    path('products/', ProductListApiView.as_view(), name='product-list'),
    path('products/<slug:slug>/', ProductDetailApiView.as_view(), name='product-detail'),

]
