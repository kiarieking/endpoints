from rest_framework import serializers
from .models import Product, Category, OrderProduct, WishList, Buyer
from django.contrib.auth import get_user_model

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'short_description', 'brand', 'unit_cost', 'featured_image_url')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)


class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = ('product', 'buyer', 'quantity', 'amount',)


class WishListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishList
        fields = ('product', 'buyer')


UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyer
        fields = ('id', 'email', 'username', 'password')
