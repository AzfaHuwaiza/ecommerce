from django.urls import path
from .views import *

from store.controller.authview import *
from store.controller.cart import *
from store.controller.wishlist import *
from store.controller.gudang import *
from store.controller import checkout, order


urlpatterns = [
    path('', home, name="home"),
    path('collections/', collections, name="collections"),
    path('collections/<str:slug>', collectionsview, name="collectionsview"),
    path('collections/<str:cate_slug>/<str:prod_slug>',
         productview, name="productview"),

    # Profile
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/edit/', ubah_profile, name='ubah_profile'),


    # Data Pelanggan
    path('data-pelanggan/', data_pelanggan, name='data_pelanggan'),
    path('data-pelanggan/<int:pk>/edit',
         ubah_data_pelanggan, name='ubah_data_pelanggan'),
    path('data-pelanggan/<int:pk>/hapus',
         hapus_data_pelanggan, name='hapus_data_pelanggan'),


    path('gudang/', gudang, name="gudang"),
    path('gudang/bahan/', gudang_bahan, name="gudang_bahan"),
    path('gudang/kategori/', gudang_kategori, name="gudang_kategori"),
    path('gudang/produk/', gudang_produk, name="gudang_produk"),

    # Create
    path('gudang/bahan/tambah/',
         tambah_bahan, name='tambah_bahan'),
    path('gudang/kategori/tambah/',
         tambah_kategori, name='tambah_kategori'),
    path('gudang/produk/tambah/',
         tambah_produk, name='tambah_produk'),


    # Update
    path('gudang/bahan/ubah/<int:id_bahan>',
         ubah_bahan, name='ubah_bahan'),
    path('gudang/kategori/ubah/<int:id_kategori>',
         ubah_kategori, name='ubah_kategori'),
    path('gudang/produk/ubah/<int:id_produk>',
         ubah_produk, name='ubah_produk'),


    # Delete
    path('produk/bahan/<int:id_bahan>',
         hapus_bahan, name='hapus_bahan'),
    path('produk/kategori/<int:id_kategori>',
         hapus_kategori, name='hapus_kategori'),
    path('produk/hapus/<int:id_produk>',
         hapus_produk, name='hapus_produk'),

    path('product-list', productlistAjax),
    path('searchproduct', searchproduct, name='searchproduct'),

    path('accounts/register/', register, name="register"),
    path('accounts/login/', loginpage, name="loginpage"),
    path('logout/', logoutpage, name="logout"),

    path('add-to-cart', addtocart, name="addtocart"),
    path('cart/', viewcart, name="cart"),
    path('update-cart', updatecart, name="updatecart"),
    path('delete-cart-item', deletecartitem, name="deletecartitem"),

    path('add-to-wishlist', addtowishlist, name="addtowishlist"),
    path('wishlist/', index, name="wishlist"),
    path('delete-wishlist-item', deletewishlistitem,
         name="deletewishlistitem"),

    path('chechout/', checkout.index, name="chechout"),
    path('place-order', checkout.placeorder, name="placeorder"),

    path('my-orders/', order.index, name="myorders"),
    path('view-orders/<str:t_no>', order.vieworder, name="orderview"),
    path('cancel-orders/<str:t_no>/',
         order.cancel_order, name='order.cancel'),

    path('403/', forbidden, name="forbidden"),

]
