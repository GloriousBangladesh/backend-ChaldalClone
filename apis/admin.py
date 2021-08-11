from django.contrib import admin
from django.contrib.admin.decorators import register
# from apis.models import (
#     ParentCategory,
#     Product
# )

from apis.models import (
    Order,
    Product
)


# Register your models here.
# admin.site.register(ParentCategory)
admin.site.register(Product)
admin.site.register(Order)
