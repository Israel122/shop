from django.shortcuts import render
from rest_framework import generics

from shop.models import Transaction, Category, Product, Cart, CartItem, Order
from shop.serilizers.shop_serializer import TransactionSerializer, CategorySerializer, ProductSerializer, CartSerializer, CartItemSerializer, OrderSerializer


class TransactionView(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


# class UpdateTransaction(generics.UpdateAPIView):
#     queryset = Transaction.objects.all()
#     serializer_class = TransactionSerializer


class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# class UpdateCategory(generics.UpdateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer


class ProductView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# class UpdateProductView(generics.UpdateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer


class CartView(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class CartItemView(generics.ListCreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer


class OrderView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
