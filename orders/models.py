from django.db import models
from cart.models import Cart
from products.models import Product
from django.db.models.signals import pre_save,post_save
from .utils import unique_order_id_generator
import string
from django.contrib.auth.models import User

class OrderHistory(models.Model):
	products=models.ForeignKey(Product,null=True,blank=True,on_delete=models.CASCADE)
	users=models.ForeignKey(User,on_delete=models.CASCADE)
	def __str__(self):
		return str(self.id)
# import stripe
# from django.conf import settings
# from users.models import Address
# from django_countries.fields import CountryField

# Create your models here.
order_status_choice=(
	('created','Created'),
	('paid','Paid'),
	('cash','cash'),
	('shipped','Shipped'),
	('refunded','Refunded'),
	)

class Order(models.Model):
	cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
	order_id=models.CharField(max_length=10,null=True,blank=True)
	users=models.ForeignKey(User,on_delete=models.CASCADE)
	# address=models.ForeignKey(Address,on_delete=models.CASCADE)
	total=models.DecimalField(max_digits=20,decimal_places=10,default=00.00)
	status=models.CharField(max_length=10,choices=order_status_choice)

	

	def __str__(self):
		
		return str(self.order_id)

	def update_total(self):
		total=self.cart.total
		print(total)
		return total


def pre_save_create_order_id(sender, instance, *args, **kwargs): 
	if not instance.order_id:
		instance.order_id = unique_order_id_generator()

pre_save.connect(pre_save_create_order_id,sender=Order)



# def pre_save_order_total_receiver(sender,instance,*args,**kwargs):
# 	if not instance.total:
# 		instance.total=instance.update_total(self.cart.total)
# 		print("toaaaaaal")
# pre_save.connect(pre_save_order_total_receiver,sender=Order)
