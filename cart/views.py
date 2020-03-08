from django.shortcuts import render,redirect
from .models import Cart
from products.models import Product

# Create your views here.
def cart_home(request):
	cart_obj,new_obj=Cart.objects.new_or_get(request)
	products=cart_obj.products.all()
	
	context={
	'products':products,
	'cart':cart_obj,
	}
	return render(request,'cart/cart_home.html',context)

def cart_remove(request):
	product_id=request.GET.get('product_id')
	try:
		prod=Product.objects.get(id=product_id)
	except:
		prod=None
		print('prod not exist')
	cart_obj,new_obj=Cart.objects.new_or_get(request)
	if prod  in cart_obj.products.all():
		cart_obj.products.remove(prod)
	
	request.session['total_item']=cart_obj.products.count()
	
	return redirect('/cart/cart_home')


def cart_update(request):
	product_id=request.GET.get('product_id')
	try:
		prod=Product.objects.get(id=product_id)
	except:
		prod=None
		print('prod not exist')
	cart_obj,new_obj=Cart.objects.new_or_get(request)
	if prod not in cart_obj.products.all():
		cart_obj.products.add(prod)
	else:
		print("if products exist in cart increase th qty")
		
		
	request.session['total_item']=cart_obj.products.count()

	return redirect('/cart/cart_home')