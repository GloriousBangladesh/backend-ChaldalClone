from django.urls import path, include
from rest_framework import routers 
from . import views

# routers where our apis are servered. 
router = routers.DefaultRouter()                   
router.register('categories', views.ParentCategoryView, 'category')
router.register('products', views.ProductView, 'products')

# api rot page url for the link http://127.0.0.1:8000/api/
urlpatterns = [
    path('', include(router.urls)),
]