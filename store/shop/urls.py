from django.urls import path

from shop.models import Transaction
from shop.views import TransactionView, CategoryView, ProductView, CartView, CartItemView, OrderView

urlpatterns = [
    path('transaction', TransactionView.as_view()),
    path('category', CategoryView.as_view()),
    path('product', ProductView.as_view()),
    path('cart', CartView.as_view()),
    path('cartitem', CartItemView.as_view()),
    path('order', OrderView.as_view())
]