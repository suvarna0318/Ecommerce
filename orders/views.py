from django.shortcuts import render,redirect
from .models import Order
from cart.models import Cart
from users.models import Address
from users.forms import AddressForm
from django.contrib.auth.decorators import login_required
import stripe
from django.conf import settings
from django.contrib import messages
stripe.api_key='sk_test_B3Z1YvMT6Ve2uDSWFnjVNEod00OXtlkHa8'

def order_display(request):
    

    return render(request,'orders/order_view.html',context={'user':request.user,})

   
    


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
    


@login_required
def checkout(request):

    cart_id=request.session.get('cart_id',None)
    add_obj=None
    cart=Cart.objects.get(id=cart_id)

    order_obj=Order.objects.filter(cart=cart_id)
    if order_obj:
        order_obj.cart=cart
        order_obj.status="created"
        order_obj.total=cart.total
        # order_obj.save()
        print("exit order",order_obj)
    else:
        
        order_obj=Order.objects.create(cart=cart,status="created",total=cart.total)
    
    try:
        add_obj=Address.objects.get(user=request.user)

        # print(add_obj.city)
        # print(add_obj.city)
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
    # result = request.GET.get('total', None)
    # print("result from ajax",result)
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
        cart_id=request.session.get('cart_id',None)
        # cart=Cart.objects.get(id=cart_id)
        order_obj=Order.objects.get(cart=cart_id)
    
        order_obj.status="paid"
        order_obj.save()
        del request.session['cart_id']
        
        request.session['total_item']=" "
        messages.success(request,'Payment Successful!')

        # send_mail("Ecommerce order","you have ordered the product",
        #     'suvarna0318@gmail.com',
        #     ['ambruth.n84@gmail.com'],fail_silently=False)

        return render(request,'orders/payment_done.html',context={})

def cash_on_delivery(request):
    if request.method == "POST":
        radoption = str(request.POST["radoption"])

        cart_id=request.session.get('cart_id',None)
        cart=Cart.objects.get(id=cart_id)
        order_obj=Order.objects.get(cart=cart_id)
    
        order_obj.status="cash"
        order_obj.save()
        
        del request.session['cart_id']
        request.session['total_item']=" "
        messages.success(request,'Your Order has been placed by cash on delivery')
    else:
        print("network issue")

    return render(request,'orders/payment_done.html',context={'cash':"cash payment",})


