from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

# Create your models here.
class UserRegisterForm(UserCreationForm):
	email=forms.EmailField()
	class Meta:
		model=User
		fields=['username','email','password1','password2']

class UserUpdateForm(forms.ModelForm):
	email=forms.EmailField()
	class Meta:
		model=User
		fields=['username','email']

class UserImageUpdateForm(forms.ModelForm):
	
	class Meta:
		model=Profile
		fields=['image']


class AddressForm(forms.Form):
	phone_num=forms.IntegerField()
	address1= forms.CharField(max_length=100)
	address2=forms.CharField(max_length=100)
	city=forms.CharField(max_length=100)
	state=forms.CharField(max_length=100)
	pincode=forms.IntegerField()

