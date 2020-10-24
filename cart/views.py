from django.shortcuts import render,redirect
from .models import Cart,PromoCode
from products.models import Product
from django.contrib import messages

# Create your views here.
def cart_home(request):
	cart_obj,new_obj=Cart.objects.new_or_get(request)
	print("1:",cart_obj)
	products=cart_obj.products.all()
	
	context={
	'products':products,
	'cart':cart_obj,
	}
	print("2:",cart_obj)
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
	print("cart-update 1:",cart_obj)
	
	if prod not in cart_obj.products.all():
		cart_obj.products.add(prod)
	else:
		print("if products exist in cart increase th qty")
		print("already exist in cart")
		if cart_obj.qty==1:
			print("increase one")
			cart_obj.qty+=1

			cart_obj.save()

		
		print("qty added:", 1)
		
				
	request.session['total_item']=cart_obj.products.count()
	print("cart-update 2:",cart_obj)
	return redirect('/products')

def qty_change(request):
		qty=request.GET.get('qty')
		print(qty)
		print("hello")
		return redirect('/cart/cart-home')


def coupen_apply(request):
    code=request.POST.get('code')
    coupen_obj=PromoCode.objects.filter(code=code)
    cart_id=request.session['cart_id']
    cart_obj=Cart.objects.get(id=cart_id)
    products=cart_obj.products.all()
    
    if coupen_obj:
    	try:
    		coupen_obj=PromoCode.objects.get(code=code,active=True)
    		print(coupen_obj.amt,cart_obj.total)
    		
    		if cart_obj.total<500:
    			messages.success(request,'coupen cannot be applied to this cart')
    			return redirect('/cart/cart-home')

    		total_amt=cart_obj.total-coupen_obj.amt
    		
    		coupen_amt=coupen_obj.amt
    		print("cart obj:",cart_obj.sub_total,cart_obj.total)
    		cart_obj.total=total_amt
    		cart_obj.save()
    		print("cart obj:",cart_obj.sub_total,cart_obj.total)
    		
    		context={
    		'products':products,
    		'cart':cart_obj,
    		'coupen_amt':coupen_amt,
    		'total':total_amt,
    		}
    		
    		print(coupen_obj.amt,coupen_obj.active)
    		messages.success(request,'Applied')
    		return render(request,'cart/cart_home.html',context)

    	except Exception as e:
    		coupen_obj=PromoCode.objects.get(code=code,active=False)
    		messages.success(request,'Already used')
    else:
		
    	print("enter correct")
    	messages.success(request,'Enter correct code')
    return redirect('/cart/cart-home')
    

    
