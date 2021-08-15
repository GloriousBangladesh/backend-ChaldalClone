from rest_framework import viewsets
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
import jwt
import time
from .serializers import ProductSerializer
import traceback
from .models import Order, Product
from users.models import User

class ProductView(viewsets.ModelViewSet):
    ''' Class to sent json data transfromed by ProductSerializer model '''
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


def search_products_by_name(request):
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
        # print("asdsa")
        token = request.COOKIES.get('jwt')
        print(token)

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = User.objects.filter(id=payload['id']).first()
        data = request.data
        
        try:
            cart_data = user.cart
            order_name = str(time.ctime()) + " | " + str(user.name[:20]) + " | " + str(user.email[:20])
            description = order_name + "\nAddress: " + data['address'] + '\n'
            total_price = 0

            for i, item in enumerate(cart_data):
                price = float(item['price']) * float(str(item['amount']))
                price = float("{:.2f}".format(price))
                temp = "\n" + str(i+1) + '. '
                temp += '\n\tid' + ": " + str(item['id'])
                temp += '\n\t title' + ": " + str(item['title'])
                temp += '\n\t measure' + ": " + str(item['measure'])
                temp += '\n\t amount' + ": " + str(item['amount'])
                temp += '\n\t price' + ": " + str(item['price']) + "x" + str(item['amount']) + " = " + str(price)
                description += temp
                total_price += price
            
            
            print(user.cart)
            print(request.data)
            print("\n\n")
            print(description)
            # user.cart = request.data
            # user.save()

            Order.objects.create(title=order_name, description=description, total_price=total_price)
            user.cart = {}
            user.save()
            return JsonResponse({
                "message": "success"
            })
        
        except:
            print(traceback.format_exc())
            user.cart = {}
            user.save()
            return JsonResponse({
                "message": "Invalid request or server error"
            })


class CheckOrders(APIView):
    def post(self, request):
        token = request.COOKIES.get('jwt')
        print(token)

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
            # print(payload)
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            query = request.data.get('user_id', '0')
            print(request.data)
            results = Order.objects.filter(user__in=User.objects.filter(id__exact=query)).values()
            # print(query)
            responseData = {
                'result': results
            }

            return JsonResponse({
                "query": query,
                "result": list(results)
            })
        except:
            print(traceback.format_exc())
    
            return JsonResponse({
                "query": "",
                "error": "user_id:<value> (in a post request) is required!"
            })