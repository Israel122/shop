
from rest_framework import serializers
from serilizers.account_serializer import AddressSerializer
from shop.models import Category, Order, Transaction, CartItem, Cart, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        field = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        field = "__all__"


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        field = "__all__"

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        field = "__all__"


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        field = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        field = "__all__"