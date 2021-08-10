from rest_framework import viewsets
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime
import time
from .serializers import ProductSerializer
from .models import Product
from users.models import User

class ProductView(viewsets.ModelViewSet):
    ''' Class to sent json data transfromed by ProductSerializer model '''
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


def search_products(request):
    if request.method == "GET":
        query = request.GET['q']
        results = Product.objects.defer('description').filter(title__contains=query).values()
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
        "error": "?q=<value> is required!"
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
        "error": "?q=<value> is required!"
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
        "error": "?id=<value> is required!"
    })


class AddOrderView(APIView):

    def post(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = User.objects.filter(id=payload['id']).first()
        
        data = request.data
        cart_data = user.cart
        order_name = str(time.ctime()) + " | " + str(user.name[:20]) + " | " + str(user.email[:75])
        description = str(time.ctime()) + '\n' + str(user.name[:20]) + " - " + str(user.email[:75]) + " - " + data['address'] + '\n'
        description += str(cart_data)

        total_price = 123
        
        print(user.cart)
        print(request.data)
        user.cart = request.data
        user.save()
        return JsonResponse({
            "message": "success"
        })