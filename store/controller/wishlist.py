from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from user_agents import parse

from django.contrib.auth.decorators import login_required

from store.models import Produk, Wishlist


@login_required(login_url='loginpage')
def index(request):
    user_agent = request.META.get('HTTP_USER_AGENT', '')
    device_type = parse(user_agent)

    if device_type.is_mobile:
        if device_type.device.family == 'iPhone' or device_type.os.family == 'Android':
            template_name = 'store/mobile/wishlist.html'
        else:
            template_name = 'store/mobile/wishlist.html'
    elif device_type.is_tablet:
        if device_type.device.family == 'iPad' or device_type.os.family == 'Android':
            template_name = 'store/tablet/wishlist.html'
        else:
            template_name = 'store/tablet/wishlist.html'
    elif device_type.is_pc:
        if device_type.os.family == 'Mac OS X' or device_type.os.family == 'Windows':
            template_name = 'store/desktop/wishlist.html'
        else:
            template_name = 'store/desktop/wishlist.html'
    else:
        template_name = 'store/desktop/wishlist.html'

    wishlist = Wishlist.objects.filter(user=request.user)
    context = {'wishlist': wishlist}
    return render(request, template_name, context)


def addtowishlist(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id'))
            product_check = Produk.objects.get(id=prod_id)
            if (product_check):
                if (Wishlist.objects.filter(user=request.user, product_id=prod_id)):
                    return JsonResponse({'status': "Product already in wishlist"})
                else:
                    Wishlist.objects.create(
                        user=request.user, product_id=prod_id)
                    return JsonResponse({'status': "Product added to wishlist"})
            else:
                return JsonResponse({'status': "No such product found"})
        else:
            return JsonResponse({'status': "Login to Continue"})
    return redirect('/')


def deletewishlistitem(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id'))

            if (Wishlist.objects.filter(user=request.user, product_id=prod_id)):
                wishlistitem = Wishlist.objects.get(
                    product_id=prod_id, user=request.user)
                wishlistitem.delete()
                return JsonResponse({'status': "Product removed from wishlist"})
            else:
                return JsonResponse({'status': "Product not found in wishlist"})
        else:
            return JsonResponse({'status': "Login to Continue"})

    return redirect('/')
