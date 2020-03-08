from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Product
from django.core.paginator import Paginator

# Create your views here.
class ProductListView(ListView):
	model=Product
	template_name='products/product_home.html'
	context_object_name='items'
	paginate_by = 4

	def get_queryset(self):
		return Product.objects.all()


class ProductDetailView(DetailView):
	model=Product
	template_name='products/detail.html'

	def get_context_data(self,*args,**kwargs):
		context=super(ProductDetailView,self).get_context_data(*args,**kwargs)
		# cart_obj,new_obj=Cart.objects.new_or_get(self.request)
		# context['cart']=cart_obj
		
		return context