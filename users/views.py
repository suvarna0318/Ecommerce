from django.shortcuts import render,redirect
from .forms import UserRegisterForm,UserUpdateForm,UserImageUpdateForm
from django.contrib import messages
# Create your views here.
def register(request):
	if request.method=='POST':
		form=UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request,f'accoount created now u can login')
			return redirect('login')
	else:

		form=UserRegisterForm()
	context={
	'form':form,

	}
	return render(request,'users/register.html',context)

def profile(request):
	if request.method=='POST':
		u_form=UserUpdateForm(request.POST,instance=request.user)
		p_form=UserImageUpdateForm(request.POST,request.FILES,instance=request.user.profile)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request,f'profile updated')
			return redirect('profile')
	else:
		u_form=UserUpdateForm(instance=request.user)
		p_form=UserImageUpdateForm(instance=request.user.profile)
	context={
	'u_form':u_form,
	'p_form':p_form,
	
	}
	return render(request,'users/profile.html',context)

def contact(request):
	print("contact page")
	return render(request,'users/contact.html')

def about(request):
	return render(request,'users/about.html')