from rest_framework import serializers
from .models import (
    ParentCategory,
    Product
)

class ParentCategorySerializer(serializers.ModelSerializer):
    ''' Class to transfrom data of collected by theParentCategory model in db.sqlite3
    to json. '''

    class Meta:
        model = ParentCategory
        fields = ('id', 'category',)

class ProductSerializer(serializers.ModelSerializer):
    ''' Class to transfrom data of collected by Product model in db.sqlite3 to json. '''

    class Meta:
        model = Product
        fields = ('category', 'id', 'name', 'measure', 'price', 'slug')