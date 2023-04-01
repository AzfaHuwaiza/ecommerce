from django.db.models.signals import post_save
from django.dispatch import receiver


from django.http.response import JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from user_agents import parse

from django.contrib import messages
from .models import *
from store.forms import FormProfile, FormUser, FormEditProfile, FormEditUser


# Create your views here.

class ProfileView(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        user_agent = request.META.get('HTTP_USER_AGENT', '')
        device_type = parse(user_agent)

        if device_type.is_mobile:
            if device_type.device.family == 'iPhone' or device_type.os.family == 'Android':
                template_name = 'store/mobile/profiles/profile.html'
            else:
                template_name = 'store/mobile/profiles/profile.html'
        elif device_type.is_tablet:
            if device_type.device.family == 'iPad' or device_type.os.family == 'Android':
                template_name = 'store/tablet/profiles/profile.html'
            else:
                template_name = 'store/tablet/profiles/profile.html'
        elif device_type.is_pc:
            if device_type.os.family == 'Mac OS X' or device_type.os.family == 'Windows':
                template_name = 'store/desktop/profiles/profile.html'
            else:
                template_name = 'store/desktop/profiles/profile.html'
        else:
            template_name = 'store/desktop/profiles/profile.html'
        pass

        return render(request, template_name)


@login_required(login_url='loginpage')
def ubah_profile(request):
    user_agent = request.META.get('HTTP_USER_AGENT', '')
    device_type = parse(user_agent)

    if device_type.is_mobile:
        if device_type.device.family == 'iPhone' or device_type.os.family == 'Android':
            template_name = 'store/mobile/profiles/edit-profile.html'
        else:
            template_name = 'store/mobile/profiles/edit-profile.html'
    elif device_type.is_tablet:
        if device_type.device.family == 'iPad' or device_type.os.family == 'Android':
            template_name = 'store/tablet/profiles/edit-profile.html'
        else:
            template_name = 'store/tablet/profiles/edit-profile.html'
    elif device_type.is_pc:
        if device_type.os.family == 'Mac OS X' or device_type.os.family == 'Windows':
            template_name = 'store/desktop/profiles/edit-profile.html'
        else:
            template_name = 'store/desktop/profiles/edit-profile.html'
    else:
        template_name = 'store/desktop/profiles/edit-profile.html'

    user = request.user
    profile = user.profile

    if request.method == 'POST':
        user_form = FormEditUser(request.POST, instance=user)
        profile_form = FormEditProfile(request.POST, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile anda sukses!')
            return redirect('profile')
    else:
        user_form = FormEditUser(instance=user)
        profile_form = FormEditProfile(instance=profile)

    context = {'user_form': user_form, 'profile_form': profile_form}
    return render(request, template_name, context)

   


def home(request):
    user_agent = request.META.get('HTTP_USER_AGENT', '')
    device_type = parse(user_agent)

    if device_type.is_mobile:
        if device_type.device.family == 'iPhone' or device_type.os.family == 'Android':
            template_name = 'store/mobile/index.html'
        else:
            template_name = 'store/mobile/index.html'
    elif device_type.is_tablet:
        if device_type.device.family == 'iPad' or device_type.os.family == 'Android':
            template_name = 'store/tablet/index.html'
        else:
            template_name = 'store/tablet/index.html'
    elif device_type.is_pc:
        if device_type.os.family == 'Mac OS X' or device_type.os.family == 'Windows':
            template_name = 'store/desktop/index.html'
        else:
            template_name = 'store/desktop/index.html'
    else:
        template_name = 'store/desktop/index.html'

    trending_products = Produk.objects.filter(trending=1)
    context = {'trending_products': trending_products,
               'template_name': template_name}
    return render(request, template_name, context)


def collections(request):
    user_agent = request.META.get('HTTP_USER_AGENT', '')
    device_type = parse(user_agent)

    if device_type.is_mobile:
        if device_type.device.family == 'iPhone' or device_type.os.family == 'Android':
            template_name = 'store/mobile/collections.html'
        else:
            template_name = 'store/mobile/collections.html'
    elif device_type.is_tablet:
        if device_type.device.family == 'iPad' or device_type.os.family == 'Android':
            template_name = 'store/tablet/collections.html'
        else:
            template_name = 'store/tablet/collections.html'
    elif device_type.is_pc:
        if device_type.os.family == 'Mac OS X' or device_type.os.family == 'Windows':
            template_name = 'store/desktop/collections.html'
        else:
            template_name = 'store/desktop/collections.html'
    else:
        template_name = 'store/desktop/collections.html'

    category = Kategori.objects.filter(status=0)
    context = {'category': category}
    return render(request, template_name, context)


def collectionsview(request, slug):
    user_agent = request.META.get('HTTP_USER_AGENT', '')
    device_type = parse(user_agent)

    if (Kategori.objects.filter(slug=slug, status=0)):

        if device_type.is_mobile:
            if device_type.device.family == 'iPhone' or device_type.os.family == 'Android':
                template_name = 'store/mobile/products/index.html'
            else:
                template_name = 'store/mobile/products/index.html'
        elif device_type.is_tablet:
            if device_type.device.family == 'iPad' or device_type.os.family == 'Android':
                template_name = 'store/tablet/products/index.html'
            else:
                template_name = 'store/tablet/products/index.html'
        elif device_type.is_pc:
            if device_type.os.family == 'Mac OS X' or device_type.os.family == 'Windows':
                template_name = 'store/desktop/products/index.html'
            else:
                template_name = 'store/desktop/products/index.html'
        else:
            template_name = 'store/desktop/products/index.html'

        products = Produk.objects.filter(kategori__slug=slug)
        category = Kategori.objects.filter(slug=slug).first()
        context = {'products': products, 'category': category}
        return render(request, template_name, context)
    else:
        messages.warning(request, "Tidak ada kategori yang ditemukan")
        return redirect('collections')


def productview(request, cate_slug, prod_slug):
    user_agent = request.META.get('HTTP_USER_AGENT', '')
    device_type = parse(user_agent)

    if device_type.is_mobile:
        if device_type.device.family == 'iPhone' or device_type.os.family == 'Android':
            template_name = 'store/mobile/products/view.html'
        else:
            template_name = 'store/mobile/products/view.html'
    elif device_type.is_tablet:
        if device_type.device.family == 'iPad' or device_type.os.family == 'Android':
            template_name = 'store/tablet/products/view.html'
        else:
            template_name = 'store/tablet/products/view.html'
    elif device_type.is_pc:
        if device_type.os.family == 'Mac OS X' or device_type.os.family == 'Windows':
            template_name = 'store/desktop/products/view.html'
        else:
            template_name = 'store/desktop/products/view.html'
    else:
        template_name = 'store/desktop/products/view.html'

    if (Kategori.objects.filter(slug=cate_slug, status=0)):
        if (Produk.objects.filter(slug=prod_slug, status=0)):
            products = Produk.objects.filter(slug=prod_slug, status=0).first()
            context = {'products': products}
        else:
            messages.error(request, "Tidak ada produk yang ditemukan")
            return redirect('collections')
    else:
        messages.error(request, "Tidak ada kategori yang ditemukan")
        return redirect('collections')
    return render(request, template_name, context)


def productlistAjax(request):
    products = Produk.objects.filter(
        status=0).values_list('name', flat=True)

    productsList = list(products)

    return JsonResponse(productsList, safe=False)


def searchproduct(request):
    if request.method == 'POST':
        searchedterm = request.POST.get('productsearch')
        if searchedterm == "":
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            product = Produk.objects.filter(
                name__contains=searchedterm).first()
            if product:
                return redirect('collections'+'/'+product.kategori.slug+'/'+product.slug)
            else:
                messages.info(
                    request, "Tidak ada produk yang cocok dengan pencarian Anda")
                return redirect(request.META.get('HTTP_REFERER'))

    return redirect(request.META.get('HTTP_REFERER'))


def forbidden(request):
    return render(request, 'store/desktop/forbidden.html')


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance, name=instance.username)


@login_required(login_url='loginpage')
def data_pelanggan(request):
    user_agent = request.META.get('HTTP_USER_AGENT', '')
    device_type = parse(user_agent)

    if device_type.is_mobile:
        if device_type.device.family == 'iPhone' or device_type.os.family == 'Android':
            template_name = 'store/mobile/profiles/data-pelanggan.html'
        else:
            template_name = 'store/mobile/profiles/data-pelanggan.html'
    elif device_type.is_tablet:
        if device_type.device.family == 'iPad' or device_type.os.family == 'Android':
            template_name = 'store/tablet/profiles/data-pelanggan.html'
        else:
            template_name = 'store/tablet/profiles/data-pelanggan.html'
    elif device_type.is_pc:
        if device_type.os.family == 'Mac OS X' or device_type.os.family == 'Windows':
            template_name = 'store/desktop/profiles/data-pelanggan.html'
        else:
            template_name = 'store/desktop/profiles/data-pelanggan.html'
    else:
        template_name = 'store/desktop/profiles/data-pelanggan.html'

    if request.user.is_superuser:
        pelanggan = User.objects.prefetch_related('profile')
        context = {'pelanggan': pelanggan}

        return render(request, template_name, context)
    else:
        return render(request, 'store/desktop/forbidden.html')


@login_required(login_url='loginpage')
def ubah_data_pelanggan(request, pk):
    user_agent = request.META.get('HTTP_USER_AGENT', '')
    device_type = parse(user_agent)

    if device_type.is_mobile:
        if device_type.device.family == 'iPhone' or device_type.os.family == 'Android':
            template_name = 'store/mobile/profiles/edit-data-pelanggan.html'
        else:
            template_name = 'store/mobile/profiles/edit-data-pelanggan.html'
    elif device_type.is_tablet:
        if device_type.device.family == 'iPad' or device_type.os.family == 'Android':
            template_name = 'store/tablet/profiles/edit-data-pelanggan.html'
        else:
            template_name = 'store/tablet/profiles/edit-data-pelanggan.html'
    elif device_type.is_pc:
        if device_type.os.family == 'Mac OS X' or device_type.os.family == 'Windows':
            template_name = 'store/desktop/profiles/edit-data-pelanggan.html'
        else:
            template_name = 'store/desktop/profiles/edit-data-pelanggan.html'
    else:
        template_name = 'store/desktop/profiles/edit-data-pelanggan.html'

    if request.user.is_superuser:
        user = get_object_or_404(User, pk=pk)
        profile = user.profile

        if request.method == 'POST':
            user_form = FormUser(request.POST, instance=user)
            profile_form = FormProfile(request.POST, instance=profile)
            if user_form.is_valid() and profile_form.is_valid():
                user_form.save()
                profile_form.save()
                return redirect('data_pelanggan')

        else:
            user_form = FormUser(instance=user)
            profile_form = FormProfile(instance=profile)

        context = {'user_form': user_form, 'profile_form': profile_form}
        return render(request, template_name, context)
    else:
        return render(request, 'store/desktop/forbidden.html')


@login_required(login_url='loginpage')
def hapus_data_pelanggan(request, pk):
    if request.user.is_superuser:
        user = get_object_or_404(User, pk=pk)
        profile = user.profile
        user.delete()
        profile.delete()
        messages.success(
            request, f'Pelanggan {user.username} berhasil dihapus')
        return redirect('data_pelanggan')

    else:
        return render(request, 'store/desktop/forbidden.html')
