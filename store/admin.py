from django.contrib import admin
from .models import *
# Register your models here.


class BahanAdmin(admin.ModelAdmin):
    list_display = ['name', 'create_at']
    search_fields = ['name', ]
    list_per_page = 10


class KategoriAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'create_at']
    search_fields = ['name', ]
    list_filter = ('bahan',)
    list_per_page = 10


class ProdukAdmin(admin.ModelAdmin):
    list_display = ['name', 'small_description', 'stok', 'selling_price']
    search_fields = ['name', ]
    list_filter = ('kategori',)
    list_per_page = 10


admin.site.register(Bahan, BahanAdmin)
admin.site.register(Kategori, KategoriAdmin)
admin.site.register(Produk, ProdukAdmin)
admin.site.register(Cart)
admin.site.register(Wishlist)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Profile)
