from django.urls import path
from . import views
app_name='cart'
urlpatterns = [
    path('cart-home/', views.cart_home,name='cart-home'),
    path('cart-update/<int:id>/', views.cart_update,name='cart-update'),
    path('cart-remove/<int:id>/', views.cart_remove,name='cart-remove'),
	path('qty_change/', views.qty_change,name='qty_change'),    
    
    
    ]