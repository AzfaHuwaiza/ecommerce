from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.forms import ModelForm
from .models import *
from django import forms


class CustomUserForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control my-2', 'placeholder': 'Masukan Username'}),
    )

    email = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control my-2', 'placeholder': 'Masukan Email'}),
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control my-2', 'placeholder': 'Masukan Password'}),
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control my-2', 'placeholder': 'Masukan Password Kembali'}),
    )

    class Meta:

        model = User
        fields = ['username', 'email', 'password1', 'password2']


class FormBahan (ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control my-2', 'placeholder': 'Masukan Nama Bahan'}),
    )

    class Meta:
        model = Bahan

        fields = ['name']


class FormKategori (ModelForm):
    slug = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control my-2', 'placeholder': '*nama-kategori'}),
    )
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control my-2', 'placeholder': 'Masukan Nama Kategori'}),
    )
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={'class': 'form-control my-2', 'placeholder': 'isi dengan ( - ) jida tidak ada'}),
    )

    class Meta:
        model = Kategori
        exclude = ['release_date']

        widgets = {
            'bahan': forms.Select({'class': 'form-select my-2'}),
            'category_image': forms.FileInput({'class': 'form-control my-2'}),
            'status': forms.CheckboxInput({'class': 'form-check-input my-2'}),
            'trending': forms.CheckboxInput({'class': 'form-check-input my-2'}),
        }


class FormProduk (ModelForm):
    slug = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control my-2', 'placeholder': '*nama-produk-bagus'}),
    )
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control my-2', 'placeholder': 'Masukan Nama Produk'}),
    )
    small_description = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control my-2'}),
    )
    size = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control my-2', 'placeholder': 'isi dengan ( - ) jida tidak ada'}),
    )
    kuantitas = forms.CharField(
        widget=forms.NumberInput(
            attrs={'class': 'form-control my-2', 'placeholder': 'isi dengan ( - ) jida tidak ada'}),
    )
    stok = forms.CharField(
        widget=forms.NumberInput(
            attrs={'class': 'form-control my-2'}),
    )
    selling_price = forms.CharField(
        widget=forms.NumberInput(
            attrs={'class': 'form-control my-2'}),
    )
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={'class': 'form-control my-2'}),
    )

    class Meta:

        model = Produk
        exclude = ['release_date']

        widgets = {
            'product_image': forms.FileInput({'class': 'form-control my-2'}),
            'kategori': forms.Select({'class': 'form-select my-2'}),
            'status': forms.CheckboxInput({'class': 'form-check-input my-2'}),
            'trending': forms.CheckboxInput({'class': 'form-check-input my-2'}),
        }


class FormEditUser(ModelForm):

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control my-2'}),
    )

    email = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control my-2'}),
    )

    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control my-2'}),
    )

    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control my-2'}),
    )

    class Meta:

        model = User
        fields = ['username', 'email', 'first_name',
                  'last_name']


class FormEditProfile(ModelForm):

    address = forms.CharField(
        widget=forms.Textarea(
            attrs={'class': 'form-control my-2'}),
    )

    city = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control my-2'}),
    )

    state = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control my-2'}),
    )

    country = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control my-2'}),
    )

    tgl_lahir = forms.DateField(
        widget=forms.TextInput(
            attrs={'type': 'date', 'class': 'form-control my-2'}
        )
    )

    phone = forms.CharField(
        widget=forms.NumberInput(
            attrs={'class': 'form-control my-2'}),
    )

    pincode = forms.CharField(
        widget=forms.NumberInput(
            attrs={'class': 'form-control my-2'}),
    )

    class Meta:
        model = Profile
        fields = ['address', 'city', 'state',
                  'country', 'tgl_lahir', 'phone', 'pincode']


class FormUser(ModelForm):

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control my-2'}),
    )

    email = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control my-2'}),
    )

    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control my-2'}),
    )

    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control my-2'}),
    )

    is_active = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={'class': 'my-2'}),
        required=False
    )

    is_staff = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={'class': 'my-2'}),
        required=False
    )

    is_superuser = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={'class': 'my-2'}),
        required=False
    )

    class Meta:

        model = User
        fields = ['username', 'email', 'first_name',
                  'last_name', 'is_active', 'is_staff', 'is_superuser']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['is_active'].validation = False
        self.fields['is_staff'].validation = False
        self.fields['is_superuser'].validation = False


class FormProfile(ModelForm):

    address = forms.CharField(
        widget=forms.Textarea(
            attrs={'class': 'form-control my-2'}),
    )

    city = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control my-2'}),
    )

    state = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control my-2'}),
    )

    country = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control my-2'}),
    )

    tgl_lahir = forms.DateField(
        widget=forms.TextInput(
            attrs={'type': 'date', 'class': 'form-control my-2'}
        )
    )

    phone = forms.CharField(
        widget=forms.NumberInput(
            attrs={'class': 'form-control my-2'}),
    )

    pincode = forms.CharField(
        widget=forms.NumberInput(
            attrs={'class': 'form-control my-2'}),
    )

    class Meta:
        model = Profile
        fields = ['address', 'city', 'state',
                  'country', 'tgl_lahir', 'phone', 'pincode']
