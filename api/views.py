from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .models import Product, Category, OrderProduct
from .serializers import *
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@api_view(['GET', ])
def product_list_view(request):
    try:
        product = Product.objects.all()
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)


@api_view(['GET', ])
def all_categories(request):
    try:
        category = Category.objects.all()
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)


@api_view(['GET', ])
def get_filtered_products(request, category_name):
    try:
        category = Category.objects.filter(name=category_name).first()
        print(category)
        products = Product.objects.filter(brand__category__name=category.name)
        print(products)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


@api_view(['GET', ])
def cart(request, buyer_id):
    buyer_cart = []
    try:
        order_products = OrderProduct.objects.filter(buyer_id=buyer_id)
        # product = Product.objects.filter(id=product_id).first()
        for order_product in order_products:
            product = {'id': order_product.product_id, 'name': order_product.product.name,
                       'featured_image_url': order_product.product.featured_image_url.url,
                       'unit_cost': order_product.product.unit_cost,
                       'short_description': order_product.product.short_description, 'quantity': order_product.quantity}
            print(product)
            buyer_cart.append(product)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = ProductSerializer(buyer_cart, many=True)
        return Response(buyer_cart)


@api_view(['GET', ])
def wishlist(request, buyer_id):
    buyer_wishlist = []
    try:
        wishlists = WishList.objects.filter(buyer_id=buyer_id)

        for wishlist in wishlists:
            product = {'id': wishlist.product_id, 'name': wishlist.product.name,
                       'unit_cost': wishlist.product.unit_cost,
                       'featured_image_url': wishlist.product.featured_image_url.url
                       }
            buyer_wishlist.append(product)
    except WishList.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        return Response(buyer_wishlist)


@api_view(['POST', ])
@csrf_exempt
def add_to_cart(request):
    print(request)
    serializer = OrderProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST', ])
@csrf_exempt
def add_to_wishlist(request):
    serializer = WishListSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST', 'GET', ])
@csrf_exempt
def remove_from_cart(request, product_id):
    orderproduct = OrderProduct.objects.get(product_id=product_id)
    try:
        orderproduct.delete()
    except OrderProduct.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(status=status.HTTP_410_GONE)


@api_view(['POST', 'GET', ])
@csrf_exempt
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'please provide both username and password'}, status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'invalid credentials'}, status=status.HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key}, status=status.HTTP_200_OK)


@api_view(['POST', ])
@permission_classes((AllowAny, ))
@csrf_exempt
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        User.objects.create_user(
            serializer.initial_data['email'],
            serializer.initial_data['username'],
            serializer.initial_data['password']
        )
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
