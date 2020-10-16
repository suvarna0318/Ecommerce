from django.urls import path
from . import views

urlpatterns = [
	path('order-display/',views.order_display,name="order-display"),
    path('checkout/', views.checkout,name='checkout'),
    path('update_address/', views.update_address,name='update_address'),
    path('delivery_address/', views.delivery_address,name='delivery_address'),
    path('payment/',views.payment,name='payment'),
    path('cash_on_delivery/',views.cash_on_delivery,name='cash_on_delivery'),
    path('select_paymenet_method/',views.select_paymenet_method,name="select_paymenet_method")
   
]