from rest_framework import viewsets 
from .serializers import (
    ParentCategorySerializer,
    ProductSerializer
)
from .models import (
    ParentCategory,
    Product
)

class ParentCategoryView(viewsets.ModelViewSet):
    ''' Class to sent json data transfromed by ParentCategorySerializer model '''

    serializer_class = ParentCategorySerializer
    queryset = ParentCategory.objects.all()

class ProductView(viewsets.ModelViewSet):
    ''' Class to sent json data transfromed by ProductSerializer model '''
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
