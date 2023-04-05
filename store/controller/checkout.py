from django.shortcuts import redirect, render
from django.contrib import messages
from user_agents import parse


from django.contrib.auth.decorators import login_required
from store.models import Cart, Order, OrderItem, Produk, Profile
from django.contrib.auth.models import User

import random


@login_required(login_url='loginpage')
def index(request):
    user_agent = request.META.get('HTTP_USER_AGENT', '')
    device_type = parse(user_agent)

    if device_type.is_mobile:
        if device_type.device.family == 'iPhone' or device_type.os.family == 'Android':
            template_name = 'store/mobile/checkout.html'
        else:
            template_name = 'store/mobile/checkout.html'
    elif device_type.is_tablet:
        if device_type.device.family == 'iPad' or device_type.os.family == 'Android':
            template_name = 'store/tablet/checkout.html'
        else:
            template_name = 'store/tablet/checkout.html'
    elif device_type.is_pc:
        if device_type.os.family == 'Mac OS X' or device_type.os.family == 'Windows':
            template_name = 'store/desktop/checkout.html'
        else:
            template_name = 'store/desktop/checkout.html'
    else:
        template_name = 'store/desktop/checkout.html'

    rawcart = Cart.objects.filter(user=request.user)
    for item in rawcart:
        if item.product_qty > item.product.stok:
            Cart.objects.filter(id=item.id).delete()

    cartitems = Cart.objects.filter(user=request.user)
    total_price = 0
    for item in cartitems:
        # total_price = total_price + item.product.selling_price * item.product_qty
        item_total_price = item.product.selling_price * item.product_qty
        total_price += item_total_price
        item.item_total_price = item_total_price


    userprofile = Profile.objects.filter(user=request.user).first()

    context = {'cartitems': cartitems,
               'total_price': total_price, 'userprofile': userprofile}
    return render(request, template_name, context)


@login_required(login_url='loginpage')
def placeorder(request):
    if request.method == 'POST':

        currentuser = User.objects.filter(id=request.user.id).first()

        if not currentuser.first_name:
            currentuser.first_name = request.POST.get('fname')
            currentuser.last_name = request.POST.get('lname')
            currentuser.save()

        if not Profile.objects.filter(user=request.user):
            userprofile = Profile()
            userprofile.user = request.user
            userprofile.phone = request.POST.get('phone')
            userprofile.address = request.POST.get('address')
            userprofile.city = request.POST.get('city')
            userprofile.state = request.POST.get('state')
            userprofile.country = request.POST.get('country')
            userprofile.pincode = request.POST.get('pincode')
            userprofile.save()

        neworder = Order()
        neworder.user = request.user
        neworder.fname = request.POST.get('fname')
        neworder.lname = request.POST.get('lname')
        neworder.email = request.POST.get('email')
        neworder.phone = request.POST.get('phone')
        neworder.address = request.POST.get('address')
        neworder.city = request.POST.get('city')
        neworder.state = request.POST.get('state')
        neworder.country = request.POST.get('country')
        neworder.pincode = request.POST.get('pincode')

        neworder.payment_mode = request.POST.get('payment_mode')

        cart = Cart.objects.filter(user=request.user)
        cart_total_price = 0
        for item in cart:
            cart_total_price = cart_total_price + \
                item.product.selling_price * item.product_qty

        neworder.total_price = cart_total_price
        trackno = 'buyer'+str(random.randint(1111111, 9999999))
        while Order.objects.filter(tracking_no=trackno) is None:
            trackno = ' buyer'+str(random.randint(1111111, 9999999))

        neworder.tracking_no = trackno
        neworder.save()

        neworderitems = Cart.objects.filter(user=request.user)
        for item in neworderitems:
            OrderItem.objects.create(
                order=neworder,
                product=item.product,
                price=item.product.selling_price,
                quantity=item.product_qty,
            )

            # To decrease the product quantityfrom available stock
            orderproduct = Produk.objects.filter(id=item.product_id).first()
            orderproduct.stok = orderproduct.stok - item.product_qty
            orderproduct.save()

        # To clear user's Cart
        Cart.objects.filter(user=request.user).delete()

        messages.success(request, "Pesanan Anda telah berhasil dibuat")
    return redirect('/my-orders/')
