from django.shortcuts import render
from .models import Order
from cart.models import Cart
from users.models import Address
from users.forms import AddressForm
from django.contrib.auth.decorators import login_required
import stripe
from django.conf import settings
from django.contrib import messages
stripe.api_key=settings.STRIPE_SECRET_KEY

@login_required
def checkout(request):
    add_obj=None
    try:
        add_obj=Address.objects.get(user=request.user)
        print(add_obj.city)
        print(add_obj.city)
    except:
        
        print("create new address")
        
    
    context={
    'object':add_obj,
    }
    return render(request,'orders/checkout.html',context)
    # if request.method=='POST':
    #     form=AddressForm(request.POST)
    #     if form.is_valid() and user.is_auhtenticated():
    #         print("address available")
    # try:

    #     get_address=Address.objects.get(user=request.user)
    # except:
    #     print("add address")
    # context={
    # 'api_key':stripe.api_key,
    # 'get_address':get_address,
    # 'form':form,
    # }
    # return render(request,'orders/checkout.html',context)


def update_address(request):
    print(request.user.username)
    add_obj=None
    try:
        add_obj=Address.objects.get(user=request.user)
        if add_obj is not None:
            if request.method=='POST':
                form=AddressForm(request.POST)
                
                if form.is_valid():
                    add_obj.user=request.user
                    add_obj.phone_num=form.cleaned_data.get('phone_num')
                    add_obj.address1=form.cleaned_data.get('address1')
                    add_obj.address2=form.cleaned_data.get('address2')
                    add_obj.city=form.cleaned_data.get('city')
                    add_obj.state=form.cleaned_data.get('state')
                    add_obj.pincode=form.cleaned_data.get('pincode')
                    add_obj.save()
                    print(add_obj.city,add_obj.state)
                    return render(request,"orders/checkout.html",context={'form':form,
                        'object':add_obj,})
    except:
        print("create new")
        if request.method=='POST':
            form=AddressForm(request.POST)
            if form.is_valid():
                user=request.user
                phone_num=form.cleaned_data.get('phone_num')
                address1=form.cleaned_data.get('address1')
                address2=form.cleaned_data.get('address2')
                city=form.cleaned_data.get('city')
                state=form.cleaned_data.get('state')
                pincode=form.cleaned_data.get('pincode')
                add_obj=Address.objects.create(user=request.user,phone_num=phone_num,
                    address1=address1,address2=address2,city=city,
                    state=state,pincode=pincode)
                add_obj.save()
                print(add_obj.city,add_obj.state)
                return render(request,"orders/checkout.html",context={'form':form,
                        'object':add_obj,})
    form=AddressForm()
    context={
    'form':form,
    'object':add_obj,
    }
    return render(request,'orders/update_address.html',context)

def delivery_address(request):
    context={
    'api_key':stripe.api_key,
    }
    return render(request,"orders/payment.html",context)
        
def payment(request):
    if request.method=='POST':
        print(request.POST['stripeToken'])
        charge=stripe.Charge.create(
            amount=1000*100,
            currency='usd',
            source=request.POST['stripeToken']

        )
        print("worked")
        # send_mail("Ecommerce order","you have ordered the product",
        #     'suvarna0318@gmail.com',
        #     ['ambruth.n84@gmail.com'],fail_silently=False)

        return render(request,'orders/payment_done.html',context={})




