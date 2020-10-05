from django.shortcuts import render,redirect
from .models import Order,PromoCode
from cart.models import Cart
from users.models import Address
from users.forms import AddressForm
from django.contrib.auth.decorators import login_required
import stripe
from django.conf import settings
from django.contrib import messages
stripe.api_key='sk_test_B3Z1YvMT6Ve2uDSWFnjVNEod00OXtlkHa8'



def coupen_apply(request):
    code=request.POST.get('code')
    print(code)
    try:
        coupen_obj=PromoCode.objects.filter(code=code)
        print("exist",coupen_obj)
    except:
        print("not exist")

    if coupen_obj.count()<1:
        coupen_obj=PromoCode.objects.create(code=code)
        messages.success(request,'Applied')
        amt=100
        return redirect('/cart/cart-home')
    else:
        # coupen_obj=PromoCode.objects.filter(num=code,user=request.user)
        # # code_add.num=code
        # # code_add.save()
        messages.warning(request,'Enter Correct Code')
        print("already applied")


    return redirect('/cart/cart-home')

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
    # context={
    # 'api_key':stripe.api_key,
    # }
    return render(request,"orders/payment.html")
        
def payment(request):
    if request.method=='POST':
        print('Data:', request.POST)
        print(request.POST['stripeToken'])

        customer=stripe.Customer.create(
            
            source=request.POST['stripeToken']
        )
        charge=stripe.Charge.create(
            customer=customer,
            amount=1000*100,
            currency='usd',
            # source=request.POST['stripeToken']

        )

        messages.success(request,'Payment Successful!')
        # send_mail("Ecommerce order","you have ordered the product",
        #     'suvarna0318@gmail.com',
        #     ['ambruth.n84@gmail.com'],fail_silently=False)

        return render(request,'orders/payment_done.html',context={})

def cash_on_delivery(request):
    if request.method == "POST":
        radoption = str(request.POST["radoption"])
    print(radoption)
    messages.success(request,'Your Order has been placed by cash on delivery')

    return render(request,'orders/payment_done.html',context={'cash':"cash payment",})


