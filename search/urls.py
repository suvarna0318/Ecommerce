from django.urls import path
# from .views import SearchListView
from . import views

urlpatterns = [
    
    path('search/',views.search,name='search'),
]