from django.urls import path
from .views import ProductListView,ProductDetailView

urlpatterns = [
    path('home/', ProductListView.as_view(),name="home"),
    path('detail/<int:pk>/', ProductDetailView.as_view(),name="detail"),
   
]