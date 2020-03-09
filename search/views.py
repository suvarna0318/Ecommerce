from django.shortcuts import render
from products.models import Product
from django.views.generic import ListView

# Create your views here.
class SearchListView(ListView):
	template_name='search/result.html'

	def get_context_data(self,*args,**kwargs):
		context=super(SearchListView,self).get_context_data(*args,**kwargs)
		
		query=self.request.GET.get('q')
		context['query']=query
		
		return context

	def get_queryset(self):
		query=self.request.GET.get('q',None)
		if query is not None:
			return Product.objects.search(query)
		return Product.objects.filter(id=1)