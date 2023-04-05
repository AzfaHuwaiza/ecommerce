from django.shortcuts import render, redirect, get_object_or_404

from user_agents import parse


from store.models import Order, OrderItem


def index(request):
    user_agent = request.META.get('HTTP_USER_AGENT', '')
    device_type = parse(user_agent)

    if device_type.is_mobile:
        if device_type.device.family == 'iPhone' or device_type.os.family == 'Android':
            template_name = 'store/mobile/orders/index.html'
        else:
            template_name = 'store/mobile/orders/index.html'
    elif device_type.is_tablet:
        if device_type.device.family == 'iPad' or device_type.os.family == 'Android':
            template_name = 'store/tablet/orders/index.html'
        else:
            template_name = 'store/tablet/orders/index.html'
    elif device_type.is_pc:
        if device_type.os.family == 'Mac OS X' or device_type.os.family == 'Windows':
            template_name = 'store/desktop/orders/index.html'
        else:
            template_name = 'store/desktop/orders/index.html'
    else:
        template_name = 'store/desktop/orders/index.html'

    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    context = {'orders': orders}
    return render(request, template_name, context)


def vieworder(request, t_no):
    user_agent = request.META.get('HTTP_USER_AGENT', '')
    device_type = parse(user_agent)

    if device_type.is_mobile:
        if device_type.device.family == 'iPhone' or device_type.os.family == 'Android':
            template_name = 'store/mobile/orders/view.html'
        else:
            template_name = 'store/mobile/orders/view.html'
    elif device_type.is_tablet:
        if device_type.device.family == 'iPad' or device_type.os.family == 'Android':
            template_name = 'store/tablet/orders/view.html'
        else:
            template_name = 'store/tablet/orders/view.html'
    elif device_type.is_pc:
        if device_type.os.family == 'Mac OS X' or device_type.os.family == 'Windows':
            template_name = 'store/desktop/orders/view.html'
        else:
            template_name = 'store/desktop/orders/view.html'
    else:
        template_name = 'store/desktop/orders/view.html'

    order = Order.objects.filter(
        tracking_no=t_no).filter(user=request.user).first()
    orderitems = OrderItem.objects.filter(order=order)
    for item in orderitems:
        item_total_price = item.price * item.quantity
        item.item_total_price = item_total_price

    order_count = OrderItem.objects.filter(order=order).count()

    
    context = {'order': order, 'orderitems': orderitems,
               'order_count': order_count}
    return render(request, template_name, context)


def cancel_order(request, t_no):
    order = get_object_or_404(Order, tracking_no=t_no, user=request.user)
    if order.status != 'Cancelled':
        order.status = 'Cancelled'
        order.save()

        return redirect('myorders')

    else:
        return redirect('myorders')

def confirm_order(request):
    user_agent = request.META.get('HTTP_USER_AGENT', '')
    device_type = parse(user_agent)

    if device_type.is_mobile:
        if device_type.device.family == 'iPhone' or device_type.os.family == 'Android':
            template_name = 'store/mobile/orders/confirm.html'
        else:
            template_name = 'store/mobile/orders/confirm.html'
    elif device_type.is_tablet:
        if device_type.device.family == 'iPad' or device_type.os.family == 'Android':
            template_name = 'store/tablet/orders/confirm.html'
        else:
            template_name = 'store/tablet/orders/confirm.html'
    elif device_type.is_pc:
        if device_type.os.family == 'Mac OS X' or device_type.os.family == 'Windows':
            template_name = 'store/desktop/orders/confirm.html'
        else:
            template_name = 'store/desktop/orders/confirm.html'
    else:
        template_name = 'store/desktop/orders/confirm.html'
    if request.user.is_superuser:
        orders = Order.objects.all().order_by('-created_at')
        context = {'orders': orders}
        return render(request, template_name, context)
    
def mark_as_shipped(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    order.status = 'Shipped'
    order.save()
    return redirect('confirm_order', order_id=order_id)

