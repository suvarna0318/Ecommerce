from django.db import models
from products.models import Product
from django.contrib.auth.models import User
from django.db.models.signals import m2m_changed,pre_save

# Create your models here.
class CartManager(models.Manager):

	def new(self,user=None):
		user_obj=None
		if user is not None and user.is_authenticated():
			user_obj=user
		return self.model.objects.create(user=user_obj)


	def new_or_get(self,request):
		cart_id=request.session.get('cart_id',None)
		print("new or get:",cart_id)
		new_obj=None
		cart_obj=None
		if cart_id is  None:
			print("created new one")
			new_obj=True
			cart_obj=Cart.objects.new()
			request.session['cart_id']=cart_obj.id	
		else:
			print("cart available")
			new_obj=False
			qs=Cart.objects.filter(id=cart_id)
			print("avail cart item",qs)
			if qs.count()==1:
				cart_obj=qs.first()
				cart_obj.save()
		return cart_obj,new_obj

	
			
		



	
	

class Cart(models.Model):
	products=models.ManyToManyField(Product,null=True,blank=True)
	user=models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
	sub_total=models.DecimalField(decimal_places=2,max_digits=20,default=00.00)
	total=models.DecimalField(decimal_places=2,max_digits=20,default=00.00)
	timestamp=models.DateTimeField(auto_now_add=True)
	qty=models.IntegerField(default=1)

	objects=CartManager()

	def __str__(self):
		return str(self.id)


class PromoCode(models.Model):
    code = models.CharField(max_length=15)
    amt=models.IntegerField(default=400)
    active=models.BooleanField(default='True')
      
    def __str__(self):
    	return str(self.id)


def m2m_changed_cart_receiver(sender,instance,action,*args,**kwargs):
	if action=='post_add' or action=='post_remove' or action=='post_clear':
		products=instance.products.all()
		
		total=0
		for prod in products:
			total+=prod.price
		
			print(total)
		print(total)
		instance.sub_total=total
		
		instance.save()

m2m_changed.connect(m2m_changed_cart_receiver,sender=Cart.products.through)

def pre_save_cart_total_receiver(sender,instance,*args,**kwargs):
	instance.total=instance.sub_total


pre_save.connect(pre_save_cart_total_receiver,sender=Cart)