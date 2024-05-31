from django.urls import path
from . import views

urlpatterns = [
    path('summary/', views.cart_summary, name="cart_sum"),
    path('add/', views.cart_add, name="cart_add"),
    path('delete/', views.cart_delete, name="cart_del"),
    path('update/', views.cart_update, name="cart_update"),
]
