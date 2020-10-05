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

def cart_remove(request,id):
	product_id=id
	try:
		prod=Product.objects.get(id=product_id)
	except:
		prod=None
		print('prod not exist')
	cart_obj="1"	
	cart_obj,new_obj=Cart.objects.new_or_get(request)
	if prod  in cart_obj.products.all():
		cart_obj.products.remove(prod)
	
	request.session['total_item']=cart_obj.products.count()
	
	return redirect('/cart/cart-home')


def cart_update(request,id):
	product_id=id
	print("id:",id)
	# try:
	# 	session_id=request.session.get('cart-id',None)
	# 	print("cart-id exist",cart-id)
	# 	cart_obj=Cart.objects.get(id=session_id)
	# except Exception as e:
	# 	print("cart-id doesnot exist",e)
	# 	cart_obj=Cart.objects.create()
	# 	print(cart_obj)
	# 	request.session['cart-id']=cart_obj.id
	# 	print(request.session)
	try:
		prod=Product.objects.get(id=product_id)
		print(prod)
	except:
		prod=None
		print('prod not exist')

	cart_obj,new_obj=Cart.objects.new_or_get(request)
	print("cart:",cart_obj)
	
	if prod not in cart_obj.products.all():
		cart_obj.products.add(prod)
	else:
		print("if products exist in cart increase th qty")
		
		
	request.session['total_item']=cart_obj.products.count()

	return redirect('/cart/cart-home')

def qty_change(request):
		# qty=request.GET.get('qty')
		print("hello")
		return redirect('/cart/cart_home')