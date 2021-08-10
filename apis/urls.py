from django.urls import path, include
from rest_framework import routers 
from . import views

# routers where our apis are servered. 
router = routers.DefaultRouter()                   
# router.register('categories', views.ParentCategoryView, 'category')
router.register('products', views.ProductView, 'products')

# api rot page url for the link http://127.0.0.1:8000/api/
urlpatterns = [
    path('', include(router.urls)),
    path('search', views.search_products),
    path('category', views.search_by_category),
    path('product', views.search_product_by_id),
    path('add_order', views.AddOrderView.as_view())
]