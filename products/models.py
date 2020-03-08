from django.db import models
from PIL import Image

# Create your models here.
s_choices={
	('s','small'),
	('m','medium'),
	('l','large')
}
class Category(models.Model):
	name=models.CharField(max_length=200)
	size=models.CharField(max_length=2,choices=s_choices)

	def __str__(self):
		return self.name
class ProductManager(models.Manager):
	pass

class Product(models.Model):
	title=models.CharField(max_length=200)
	description=models.TextField()
	price=models.IntegerField()
	slug=models.SlugField(blank=True,unique=True)
	image=models.ImageField(upload_to='products_pic',default='def.jpg')
	qty=models.IntegerField(default=1)
	category=models.ForeignKey(Category,on_delete=models.CASCADE)
	

	objects=ProductManager()

	def __str__(self):
		return self.title



	def save(self,*args,**kwargs):
		super(Product,self).save(*args,**kwargs)
		img=Image.open(self.image.path)

		if img.width>200 or img.height>250:
			output_size=(200,250)
			img.thumbnail(output_size)
			img.save(self.image.path)

# def pre_save_slug_gen(sender,instance,*args,**kwargs):
# 	if not instance.slug:
# 		print(unique_slug_generator)
# 		instance.slug=unique_slug_generator()


# pre_save.connect(pre_save_slug_gen,sender=Product)

