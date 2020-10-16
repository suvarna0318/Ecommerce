from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,DetailView
from .models import Product,Category
from django.core.paginator import Paginator
from django.contrib import messages


def home(request):
	category=Category.objects.all()
	
	return render(request,'products/home.html',context={'category':category,})

# Create your views here.

class ProductListView(ListView):
	model=Product
	template_name='products/shop-grid.html'
	context_object_name='items'
	paginate_by = 16


	def get_queryset(self,**kwargs):

		return Product.objects.all()

	def get_context_data(self, *args, **kwargs):
		context = super(ProductListView, self).get_context_data(*args, **kwargs)
		category=Category.objects.all()
		
		context['category'] = category
		# print(context)
		return context

	


class ProductDetailView(DetailView):

	model=Product
	template_name='products/shop-details.html'

	def get_context_data(self,*args,**kwargs):
		context=super(ProductDetailView,self).get_context_data(*args,**kwargs)
		# cart_obj,new_obj=Cart.objects.new_or_get(self.request)
		# context['cart']=cart_obj
		print(context)
		# print(context.products)
		
		return context

def show_category_product(request,name):
	c = get_object_or_404(Category, name=name)
	print("c:",c)

	category=Category.objects.all()
	

	products = c.product_set.all() 
	if products is None:
		print("none")
		messages.success(request,"stay tunnned we will update Sooon!")
		return render(request,'products/shop-grid.html',context)
	print('products avail:',products)
	context={
	'items':products,
	'category':category,
	
	}
	return render(request,'products/shop-grid.html',context)

# @login_required
def add_to_wishlist(request):

   product = get_object_or_404(Product,slug='tomato-slug')


   wished_item,created = Wishlist.objects.get_or_create(wished_item=product,
   slug = product.slug,
   user = request.user,
   )

   messages.info(request,'The item was added to your wishlist')
   return redirect('products/home')

# def file_not_found_404(request):
#  	page_title = 'Page Not Found'
#  	return render_to_response('404.html', locals(),
#  	context_instance=RequestContext(request)) 