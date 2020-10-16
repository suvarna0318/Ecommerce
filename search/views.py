from django.shortcuts import render
from products.models import Product
from django.views.generic import ListView


def search(request):
	
	query=request.GET.get('q')	
	print(query)
	q_list=query.split(" ")#query split
	print(q_list)

	
	products=Product.objects.search(query)

	context={
	'items':products,
	}
	
	return render(request,'search/result.html',context)



# class SearchListView(ListView):
# 	template_name='products/shop-grid.html'

# 	def get_context_data(self,*args,**kwargs):
# 		context=super(SearchListView,self).get_context_data(*args,**kwargs)
# 		print(self.request.GET.get('q'))
# 		query=self.request.GET.get('q')
# 		context['query']=query
		
# 		return context

# 	def get_queryset(self):
# 		query=self.request.GET.get('q',None)
# 		if query is not None:
# 			print(Product.objects.search(query))
# 			return Product.objects.search(query)

# 		return Product.objects.filter(id=1)