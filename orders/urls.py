from django.urls import path
from . import views

urlpatterns = [
    path('checkout/', views.checkout,name='checkout'),
    path('update_address/', views.update_address,name='update_address'),
    path('delivery_address/', views.delivery_address,name='delivery_address'),
    path('payment/',views.payment,name='payment'),
    
   
]