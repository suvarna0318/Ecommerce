from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	image=models.ImageField(default='def.jpg',upload_to='profile_pictures')

	def __str__(self):
		return self.user.name

@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
	if created:
		Profile.objects.create(user=instance)


@receiver(post_save,sender=User)
def save_profile(sender,instance,**kwargs):
	instance.profile.save()



class Address(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	phone_num=models.IntegerField()
	address1=models.CharField(max_length=120)
	address2=models.CharField(max_length=120)
	city=models.CharField(max_length=120)
	state=models.CharField(max_length=120)
	pincode=models.IntegerField()

	def __str__(self):
		return self.user.username

