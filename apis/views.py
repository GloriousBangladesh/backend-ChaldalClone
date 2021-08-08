from rest_framework import viewsets
from django.http import JsonResponse
from .serializers import (
    # ParentCategorySerializer,
    ProductSerializer
)
from .models import (
    # ParentCategory,
    Product
)

# class ParentCategoryView(viewsets.ModelViewSet):
#     ''' Class to sent json data transfromed by ParentCategorySerializer model '''

#     serializer_class = ParentCategorySerializer
#     queryset = ParentCategory.objects.all()

class ProductView(viewsets.ModelViewSet):
    ''' Class to sent json data transfromed by ProductSerializer model '''
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

def search_products(request):
    if request.method == "GET":
        query = request.GET['q']
        results = Product.objects.defer('description').filter(name__contains=query).values()
        print(query)
        responseData = {
            'result': results
        }

        return JsonResponse({
            "query": query,
            "result": list(results)
        })
    else:
        pass
    
    return JsonResponse({
        "query": "",
        "error": "?u=<value> is required!"
    })

def search_by_category(request):
    if request.method == "GET":
        try:
            query = request.GET['q']
            results = Product.objects.filter(category__iexact=query).values()
            print(query)
            responseData = {
                'result': results
            }

            return JsonResponse({
                "query": query,
                "result": list(results)
            })
        except:
            pass
   
    return JsonResponse({
        "query": "",
        "error": "?u=<value> is required!"
    })

def search_product_by_id(request):
    if request.method == "GET":
        try:
            query = request.GET['id']
            results = Product.objects.filter(id__exact=query).values()
            print(query)
            responseData = {
                'result': results
            }

            return JsonResponse({
                "query": query,
                "result": list(results)
            })
        except:
            pass
   
    return JsonResponse({
        "query": "",
        "error": "?u=<value> is required!"
    })