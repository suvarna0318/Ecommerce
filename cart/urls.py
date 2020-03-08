from django.urls import path
from . import views

urlpatterns = [
    path('cart_home/', views.cart_home,name='cart_home'),
    path('cart_update/', views.cart_update,name='cart_update'),
    path('cart_remove/', views.cart_remove,name='cart_remove'),
    
    
    
    ]