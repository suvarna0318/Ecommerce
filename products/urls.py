from django.urls import path
from . import views
from .views import ProductListView,ProductDetailView

urlpatterns = [
	path('home/',views.home,name='home'),
    path('products/', ProductListView.as_view(),name="products"),
    path('detail/<int:pk>/', ProductDetailView.as_view(),name="detail"),
   
]