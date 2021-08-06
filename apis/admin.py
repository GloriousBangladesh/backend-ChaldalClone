from django.contrib import admin
from apis.models import (
    ParentCategory,
    Product
)

# Register your models here.
admin.site.register(ParentCategory)
admin.site.register(Product)
