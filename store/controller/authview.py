from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.contrib import messages
from store.forms import CustomUserForm
from user_agents import parse


# Create your views here.


def register(request):
    user_agent = request.META.get('HTTP_USER_AGENT', '')
    device_type = parse(user_agent)

    if device_type.is_mobile:
        if device_type.device.family == 'iPhone' or device_type.os.family == 'Android':
            template_name = 'store/mobile/auth/register.html'
        else:
            template_name = 'store/mobile/auth/register.html'
    elif device_type.is_tablet:
        if device_type.device.family == 'iPad' or device_type.os.family == 'Android':
            template_name = 'store/tablet/auth/register.html'
        else:
            template_name = 'store/tablet/auth/register.html'
    elif device_type.is_pc:
        if device_type.os.family == 'Mac OS X' or device_type.os.family == 'Windows':
            template_name = 'store/desktop/auth/register.html'
        else:
            template_name = 'store/desktop/auth/register.html'
    else:
        template_name = 'store/desktop/auth/register.html'

    form = CustomUserForm()
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Berhasil Regitrasi! Login untuk Melanjutkan")
            return redirect("loginpage")
    context = {'form': form}
    return render(request, template_name, context)


def loginpage(request):
    user_agent = request.META.get('HTTP_USER_AGENT', '')
    device_type = parse(user_agent)

    if device_type.is_mobile:
        if device_type.device.family == 'iPhone' or device_type.os.family == 'Android':
            template_name = 'store/mobile/auth/login.html'
        else:
            template_name = 'store/mobile/auth/login.html'
    elif device_type.is_tablet:
        if device_type.device.family == 'iPad' or device_type.os.family == 'Android':
            template_name = 'store/tablet/auth/login.html'
        else:
            template_name = 'store/tablet/auth/login.html'
    elif device_type.is_pc:
        if device_type.os.family == 'Mac OS X' or device_type.os.family == 'Windows':
            template_name = 'store/desktop/auth/login.html'
        else:
            template_name = 'store/desktop/auth/login.html'
    else:
        template_name = 'store/desktop/auth/login.html'

    if request.user.is_authenticated:
        messages.warning(request, "Kamu sudah Log In")
        return redirect("home")
    else:
        if request.method == 'POST':
            name = request.POST.get('username')
            passwd = request.POST.get('password')

            user = authenticate(request, username=name, password=passwd)

            if user is not None:
                login(request, user)
                messages.success(request, "Login Berhasil")
                return redirect("home")
            else:
                messages.error(request, "Username atau password salah")
                return redirect("loginpage")

        return render(request, template_name)


def logoutpage(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "Log Out Berhasil")
    return redirect("loginpage")
