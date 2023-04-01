from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from user_agents import parse


from django.contrib.auth.decorators import login_required

from store.models import Produk, Cart


def addtocart(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id'))
            product_check = Produk.objects.get(id=prod_id)
            if (product_check):
                if (Cart.objects.filter(user=request.user.id, product_id=prod_id)):
                    return JsonResponse({'status': "Product Already in Cart"})
                else:
                    prod_qty = int(request.POST.get('product_qty'))

                    if product_check.stok >= prod_qty:
                        Cart.objects.create(
                            user=request.user, product_id=prod_id, product_qty=prod_qty)
                        return JsonResponse({'status': "Product addedd successfully"})
                    else:
                        return JsonResponse({'status': "Only " + str(product_check.stok) + " quantity available "})
            else:
                return JsonResponse({'status': "No such product found"})
        else:
            return JsonResponse({'status': "Login to Continue"})

    return redirect('/')


@login_required(login_url='loginpage')
def viewcart(request):
    user_agent = request.META.get('HTTP_USER_AGENT', '')
    device_type = parse(user_agent)

    if device_type.is_mobile:
        if device_type.device.family == 'iPhone' or device_type.os.family == 'Android':
            template_name = 'store/mobile/cart.html'
        else:
            template_name = 'store/mobile/cart.html'
    elif device_type.is_tablet:
        if device_type.device.family == 'iPad' or device_type.os.family == 'Android':
            template_name = 'store/tablet/cart.html'
        else:
            template_name = 'store/tablet/cart.html'
    elif device_type.is_pc:
        if device_type.os.family == 'Mac OS X' or device_type.os.family == 'Windows':
            template_name = 'store/desktop/cart.html'
        else:
            template_name = 'store/desktop/cart.html'
    else:
        template_name = 'store/desktop/cart.html'

    cart = Cart.objects.filter(user=request.user)
    context = {'cart': cart}
    return render(request, template_name, context)


def updatecart(request):
    if request.method == 'POST':
        prod_id = int(request.POST.get('product_id'))
        if (Cart.objects.filter(user=request.user, product_id=prod_id)):
            prod_qty = int(request.POST.get('product_qty'))
            cart = Cart.objects.get(product_id=prod_id, user=request.user)
            cart.product_qty = prod_qty
            cart.save()
            return JsonResponse({'status': "Updated Successfully"})
    return redirect('/')


def deletecartitem(request):
    if request.method == 'POST':
        prod_id = int(request.POST.get('product_id'))
        if (Cart.objects.filter(user=request.user, product_id=prod_id)):
            cartitem = Cart.objects.get(product_id=prod_id, user=request.user)
            cartitem.delete()
        return JsonResponse({'status': "Deleted Successfully"})
    return redirect('/')
