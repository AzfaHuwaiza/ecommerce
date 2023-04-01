from django.shortcuts import redirect, render
from django.contrib import messages
from user_agents import parse


from django.contrib.auth.decorators import login_required
from store.models import Bahan, Kategori, Produk
from store.forms import *


@login_required(login_url='loginpage')
def gudang(request):
    user_agent = request.META.get('HTTP_USER_AGENT', '')
    device_type = parse(user_agent)

    if device_type.is_mobile:
        if device_type.device.family == 'iPhone' or device_type.os.family == 'Android':
            template_name = 'store/mobile/gudang/index.html'
        else:
            template_name = 'store/mobile/gudang/index.html'
    elif device_type.is_tablet:
        if device_type.device.family == 'iPad' or device_type.os.family == 'Android':
            template_name = 'store/tablet/gudang/index.html'
        else:
            template_name = 'store/tablet/gudang/index.html'
    elif device_type.is_pc:
        if device_type.os.family == 'Mac OS X' or device_type.os.family == 'Windows':
            template_name = 'store/desktop/gudang/index.html'
        else:
            template_name = 'store/desktop/gudang/index.html'
    else:
        template_name = 'store/desktop/gudang/index.html'

    if request.user.is_superuser:
        return render(request, template_name)
    elif request.user.is_staff:
        return render(request, template_name)
    else:
        return render(request, 'store/desktop/forbidden.html')


@login_required(login_url='loginpage')
def gudang_bahan(request):
    user_agent = request.META.get('HTTP_USER_AGENT', '')
    device_type = parse(user_agent)

    if device_type.is_mobile:
        if device_type.device.family == 'iPhone' or device_type.os.family == 'Android':
            template_name = 'store/mobile/gudang/bahan.html'
        else:
            template_name = 'store/mobile/gudang/bahan.html'
    elif device_type.is_tablet:
        if device_type.device.family == 'iPad' or device_type.os.family == 'Android':
            template_name = 'store/tablet/gudang/bahan.html'
        else:
            template_name = 'store/tablet/gudang/bahan.html'
    elif device_type.is_pc:
        if device_type.os.family == 'Mac OS X' or device_type.os.family == 'Windows':
            template_name = 'store/desktop/gudang/bahan.html'
        else:
            template_name = 'store/desktop/gudang/bahan.html'
    else:
        template_name = 'store/desktop/gudang/bahan.html'

    if request.user.is_superuser:
        bahan = Bahan.objects.all()
        konteks = {
            'bahans': bahan
        }
        return render(request, template_name, konteks)

    elif request.user.is_staff:
        bahan = Bahan.objects.all()
        konteks = {
            'bahans': bahan
        }
        return render(request, template_name, konteks)

    else:
        return render(request, 'store/desktop/forbidden.html')


@login_required(login_url='loginpage')
def gudang_kategori(request):
    user_agent = request.META.get('HTTP_USER_AGENT', '')
    device_type = parse(user_agent)

    if device_type.is_mobile:
        if device_type.device.family == 'iPhone' or device_type.os.family == 'Android':
            template_name = 'store/mobile/gudang/kategori.html'
        else:
            template_name = 'store/mobile/gudang/kategori.html'
    elif device_type.is_tablet:
        if device_type.device.family == 'iPad' or device_type.os.family == 'Android':
            template_name = 'store/tablet/gudang/kategori.html'
        else:
            template_name = 'store/tablet/gudang/kategori.html'
    elif device_type.is_pc:
        if device_type.os.family == 'Mac OS X' or device_type.os.family == 'Windows':
            template_name = 'store/desktop/gudang/kategori.html'
        else:
            template_name = 'store/desktop/gudang/kategori.html'
    else:
        template_name = 'store/desktop/gudang/kategori.html'

    if request.user.is_superuser:
        kategori = Kategori.objects.all()
        konteks = {
            'kategoris': kategori
        }

        return render(request, template_name, konteks)

    elif request.user.is_staff:
        kategori = Kategori.objects.all()
        konteks = {
            'kategoris': kategori
        }

        return render(request, template_name, konteks)

    else:
        return render(request, 'store/desktop/forbidden.html')


@login_required(login_url='loginpage')
def gudang_produk(request):
    user_agent = request.META.get('HTTP_USER_AGENT', '')
    device_type = parse(user_agent)

    if device_type.is_mobile:
        if device_type.device.family == 'iPhone' or device_type.os.family == 'Android':
            template_name = 'store/mobile/gudang/produk.html'
        else:
            template_name = 'store/mobile/gudang/produk.html'
    elif device_type.is_tablet:
        if device_type.device.family == 'iPad' or device_type.os.family == 'Android':
            template_name = 'store/tablet/gudang/produk.html'
        else:
            template_name = 'store/tablet/gudang/produk.html'
    elif device_type.is_pc:
        if device_type.os.family == 'Mac OS X' or device_type.os.family == 'Windows':
            template_name = 'store/desktop/gudang/produk.html'
        else:
            template_name = 'store/desktop/gudang/produk.html'
    else:
        template_name = 'store/desktop/gudang/produk.html'

    if request.user.is_superuser:
        produk = Produk.objects.all()
        konteks = {
            'produks': produk
        }

        return render(request, template_name, konteks)

    elif request.user.is_staff:
        produk = Produk.objects.all()
        konteks = {
            'produks': produk
        }

        return render(request, template_name, konteks)

    else:
        return render(request, 'store/desktop/forbidden.html')


@login_required(login_url='loginpage')
def tambah_bahan(request):
    user_agent = request.META.get('HTTP_USER_AGENT', '')
    device_type = parse(user_agent)

    if device_type.is_mobile:
        if device_type.device.family == 'iPhone' or device_type.os.family == 'Android':
            template_name = 'store/mobile/gudang/tambah/bahan.html'
        else:
            template_name = 'store/mobile/gudang/tambah/bahan.html'
    elif device_type.is_tablet:
        if device_type.device.family == 'iPad' or device_type.os.family == 'Android':
            template_name = 'store/tablet/gudang/tambah/bahan.html'
        else:
            template_name = 'store/tablet/gudang/tambah/bahan.html'
    elif device_type.is_pc:
        if device_type.os.family == 'Mac OS X' or device_type.os.family == 'Windows':
            template_name = 'store/desktop/gudang/tambah/bahan.html'
        else:
            template_name = 'store/desktop/gudang/tambah/bahan.html'
    else:
        template_name = 'store/desktop/gudang/tambah/bahan.html'

    if request.user.is_superuser:
        if request.POST:
            form = FormBahan(request.POST)
            if form.is_valid():
                form.save()
                form = FormBahan()
                pesan = "Bahan Berhasil Ditambahkan"

                konteks = {
                    'form': form,
                    'pesan': pesan,
                }
                return render(request, template_name, konteks)

        else:
            form = FormBahan()

            konteks = {
                'form': form,
            }
        return render(request, template_name, konteks)

    else:
        return render(request, 'store/desktop/forbidden.html')


@login_required(login_url='loginpage')
def tambah_kategori(request):
    user_agent = request.META.get('HTTP_USER_AGENT', '')
    device_type = parse(user_agent)

    if device_type.is_mobile:
        if device_type.device.family == 'iPhone' or device_type.os.family == 'Android':
            template_name = 'store/mobile/gudang/tambah/kategori.html'
        else:
            template_name = 'store/mobile/gudang/tambah/kategori.html'
    elif device_type.is_tablet:
        if device_type.device.family == 'iPad' or device_type.os.family == 'Android':
            template_name = 'store/tablet/gudang/tambah/kategori.html'
        else:
            template_name = 'store/tablet/gudang/tambah/kategori.html'
    elif device_type.is_pc:
        if device_type.os.family == 'Mac OS X' or device_type.os.family == 'Windows':
            template_name = 'store/desktop/gudang/tambah/kategori.html'
        else:
            template_name = 'store/desktop/gudang/tambah/kategori.html'
    else:
        template_name = 'store/desktop/gudang/tambah/kategori.html'

    if request.user.is_superuser:
        if request.POST:
            form = FormKategori(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                form = FormKategori()
                pesan = "Kategori Berhasil Ditambahkan"

                konteks = {
                    'form': form,
                    'pesan': pesan,
                }
                return render(request, template_name, konteks)

        else:
            form = FormKategori()

            konteks = {
                'form': form,
            }

        return render(request, template_name, konteks)

    else:
        return render(request, 'store/desktop/forbidden.html')


@login_required(login_url='loginpage')
def tambah_produk(request):
    user_agent = request.META.get('HTTP_USER_AGENT', '')
    device_type = parse(user_agent)

    if device_type.is_mobile:
        if device_type.device.family == 'iPhone' or device_type.os.family == 'Android':
            template_name = 'store/mobile/gudang/tambah/produk.html'
        else:
            template_name = 'store/mobile/gudang/tambah/produk.html'
    elif device_type.is_tablet:
        if device_type.device.family == 'iPad' or device_type.os.family == 'Android':
            template_name = 'store/tablet/gudang/tambah/produk.html'
        else:
            template_name = 'store/tablet/gudang/tambah/produk.html'
    elif device_type.is_pc:
        if device_type.os.family == 'Mac OS X' or device_type.os.family == 'Windows':
            template_name = 'store/desktop/gudang/tambah/produk.html'
        else:
            template_name = 'store/desktop/gudang/tambah/produk.html'
    else:
        template_name = 'store/desktop/gudang/tambah/produk.html'

    if request.user.is_superuser:
        if request.POST:
            form = FormProduk(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                form = FormProduk()
                pesan = "Produk Berhasil Ditambahkan"

                konteks = {
                    'form': form,
                    'pesan': pesan,

                }
                return render(request, template_name, konteks)

        else:
            form = FormProduk()

            konteks = {
                'form': form,
            }
        return render(request, template_name, konteks)

    else:
        return render(request, 'store/desktop/forbidden.html')


@login_required(login_url='loginpage')
def ubah_bahan(request, id_bahan):
    user_agent = request.META.get('HTTP_USER_AGENT', '')
    device_type = parse(user_agent)

    if device_type.is_mobile:
        if device_type.device.family == 'iPhone' or device_type.os.family == 'Android':
            template_name = 'store/mobile/gudang/ubah/bahan.html'
        else:
            template_name = 'store/mobile/gudang/ubah/bahan.html'
    elif device_type.is_tablet:
        if device_type.device.family == 'iPad' or device_type.os.family == 'Android':
            template_name = 'store/tablet/gudang/ubah/bahan.html'
        else:
            template_name = 'store/tablet/gudang/ubah/bahan.html'
    elif device_type.is_pc:
        if device_type.os.family == 'Mac OS X' or device_type.os.family == 'Windows':
            template_name = 'store/desktop/gudang/ubah/bahan.html'
        else:
            template_name = 'store/desktop/gudang/ubah/bahan.html'
    else:
        template_name = 'store/desktop/gudang/ubah/bahan.html'

    if request.user.is_superuser:
        bahan = Bahan.objects.get(id=id_bahan)
        if request.POST:
            form = FormBahan(request.POST, instance=bahan)
            if form.is_valid():
                form.save()
                messages.success(request, "Data Berhasil diperbaharui")
                return redirect('ubah_bahan', id_bahan=id_bahan)
        else:
            form = FormBahan(instance=bahan)
            konteks = {
                'form': form,
                'bahan': bahan,
            }
        return render(request, template_name, konteks)

    else:
        return render(request, 'store/desktop/forbidden.html')


@login_required(login_url='loginpage')
def ubah_kategori(request, id_kategori):
    user_agent = request.META.get('HTTP_USER_AGENT', '')
    device_type = parse(user_agent)

    if device_type.is_mobile:
        if device_type.device.family == 'iPhone' or device_type.os.family == 'Android':
            template_name = 'store/mobile/gudang/ubah/kategori.html'
        else:
            template_name = 'store/mobile/gudang/ubah/kategori.html'
    elif device_type.is_tablet:
        if device_type.device.family == 'iPad' or device_type.os.family == 'Android':
            template_name = 'store/tablet/gudang/ubah/kategori.html'
        else:
            template_name = 'store/tablet/gudang/ubah/kategori.html'
    elif device_type.is_pc:
        if device_type.os.family == 'Mac OS X' or device_type.os.family == 'Windows':
            template_name = 'store/desktop/gudang/ubah/kategori.html'
        else:
            template_name = 'store/desktop/gudang/ubah/kategori.html'
    else:
        template_name = 'store/desktop/gudang/ubah/kategori.html'

    if request.user.is_superuser:
        kategori = Kategori.objects.get(id=id_kategori)
        if request.method == 'POST':
            form = FormKategori(request.POST, request.FILES, instance=kategori)
            if form.is_valid():
                form.save()
                messages.success(request, "Data Berhasil diperbaharui")
                return redirect('ubah_kategori', id_kategori=id_kategori)
        else:
            form = FormKategori(instance=kategori)
            context = {
                'form': form,
                'kategori': kategori,
            }
        return render(request, template_name, context)

    else:
        return render(request, 'store/desktop/forbidden.html')


@login_required(login_url='loginpage')
def ubah_produk(request, id_produk):
    user_agent = request.META.get('HTTP_USER_AGENT', '')
    device_type = parse(user_agent)

    if device_type.is_mobile:
        if device_type.device.family == 'iPhone' or device_type.os.family == 'Android':
            template_name = 'store/mobile/gudang/ubah/produk.html'
        else:
            template_name = 'store/mobile/gudang/ubah/produk.html'
    elif device_type.is_tablet:
        if device_type.device.family == 'iPad' or device_type.os.family == 'Android':
            template_name = 'store/tablet/gudang/ubah/produk.html'
        else:
            template_name = 'store/tablet/gudang/ubah/produk.html'
    elif device_type.is_pc:
        if device_type.os.family == 'Mac OS X' or device_type.os.family == 'Windows':
            template_name = 'store/desktop/gudang/ubah/produk.html'
        else:
            template_name = 'store/desktop/gudang/ubah/bahan.html'
    else:
        template_name = 'store/desktop/gudang/ubah/produk.html'

    if request.user.is_superuser:
        produk = Produk.objects.get(id=id_produk)
        if request.method == 'POST':
            form = FormProduk(request.POST, request.FILES, instance=produk)
            if form.is_valid():
                form.save()
                messages.success(request, "Data Berhasil diperbaharui")
                return redirect('ubah_produk', id_produk=id_produk)
        else:
            form = FormProduk(instance=produk)
            context = {
                'form': form,
                'produk': produk,
            }
        return render(request, template_name, context)

    elif request.user.is_staff:
        produk = Produk.objects.get(id=id_produk)
        if request.method == 'POST':
            form = FormProduk(request.POST, request.FILES, instance=produk)
            if form.is_valid():
                form.save()
                messages.success(request, "Data Berhasil diperbaharui")
                return redirect('ubah_produk', id_produk=id_produk)
        else:
            form = FormProduk(instance=produk)
            context = {
                'form': form,
                'produk': produk,
            }
        return render(request, template_name, context)

    else:
        return render(request, 'store/desktop/forbidden.html')


@login_required(login_url='loginpage')
def hapus_bahan(request, id_bahan):
    if request.user.is_superuser:
        bahan = Bahan.objects.filter(id=id_bahan)
        bahan.delete()

        return redirect('gudang_bahan')

    else:
        return render(request, 'store/desktop/forbidden.html')


@login_required(login_url='loginpage')
def hapus_kategori(request, id_kategori):
    if request.user.is_superuser:
        kategori = Kategori.objects.filter(id=id_kategori)
        kategori.delete()

        return redirect('gudang_kategori')

    else:
        return render(request, 'store/desktop/forbidden.html')


@login_required(login_url='loginpage')
def hapus_produk(request, id_produk):
    if request.user.is_superuser:
        produk = Produk.objects.filter(id=id_produk)
        produk.delete()

        return redirect('gudang_produk')

    else:
        return render(request, 'store/desktop/forbidden.html')
