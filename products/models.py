from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.db import models
from PIL import Image
from django.utils.text import slugify
from django.db.models import Q

# Create your models here.

import random
import string

def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def unique_slug_generator(instance, new_slug=None):
    """
    This is for a Django project and it assumes your instance 
    has a model with a slug field and a title character (char) field.
    """
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
                    slug=slug,
                    randstr=random_string_generator(size=4)
                )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug

class Category(models.Model):
	name=models.CharField(max_length=200)
	

	def __str__(self):
		return self.name
class ProductManager(models.Manager):
	def search(self, query):
		print(query)
		lookups=(Q(title__icontains=query)
			|Q(description__icontains=query)
			|Q(price__icontains=query)
			|Q(slug__icontains=query))

		return self.model.objects.filter(lookups)

class Product(models.Model):
	title=models.CharField(max_length=200)
	description=models.TextField()
	price=models.IntegerField()
	slug=models.SlugField(blank=True)
	image=models.ImageField(upload_to='products_pic')
	qty=models.CharField(max_length=5)
	category=models.ForeignKey(Category,on_delete=models.CASCADE)
	is_active=models.BooleanField(default=True)
	

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



def pre_save_slug_gen(sender,instance,*args,**kwargs):
	if not instance.slug:
		print(unique_slug_generator)
		instance.slug=unique_slug_generator(instance)


pre_save.connect(pre_save_slug_gen,sender=Product)