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

    orders = Order.objects.filter(user=request.user)
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
