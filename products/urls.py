from django.urls import path
from . import views
from .views import ProductDetailView,ProductListView
# handler404 = 'products.views.file_not_found_404' 
urlpatterns = [
	path('home/',views.home,name='home'),
    path('products/', ProductListView.as_view(),name="products"),
    path('detail/<int:pk>/', ProductDetailView.as_view(),name="detail"),
    path('add_to_wishlist/',views.add_to_wishlist,name='add_to_wishlist'),
   	path('show_category_product/<str:name>/',views.show_category_product,name="show_category_product")
]