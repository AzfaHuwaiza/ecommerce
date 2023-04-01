import os
import datetime
from django.db.models import *

from django.contrib.auth.models import User
# Create your models here.


def get_file_path(requset, filename):
    original_filename = filename
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (nowTime, original_filename)
    return os.path.join('uploads/', filename)


class Bahan(Model):
    slug = CharField(max_length=150, null=False, blank=False)
    name = CharField(max_length=150, null=False, blank=False)
    create_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Kategori(Model):
    bahan = ForeignKey(Bahan, on_delete=CASCADE)
    slug = CharField(max_length=150, null=False, blank=False)
    name = CharField(max_length=150, null=False, blank=False)
    category_image = ImageField(
        upload_to=get_file_path, null=False, blank=False)
    description = TextField(max_length=500, null=True, blank=True)
    status = BooleanField(
        default=False, help_text="0=default, 1=Hidden")
    trending = BooleanField(
        default=False, help_text="0=default, 1=Trending")
    create_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Produk(Model):
    kategori = ForeignKey(Kategori, on_delete=CASCADE)
    slug = CharField(max_length=150, null=False, blank=False)
    name = CharField(max_length=150, null=False, blank=False)
    product_image = ImageField(
        upload_to=get_file_path, null=False, blank=False)
    small_description = CharField(max_length=250, null=False, blank=False)
    size = CharField(max_length=25, null=True, blank=True)
    kuantitas = IntegerField(null=True, blank=True)
    stok = IntegerField(null=False, blank=False)
    description = TextField(max_length=500, null=False, blank=False)
    selling_price = FloatField(null=False, blank=False)
    status = BooleanField(
        default=False, help_text="0=default, 1=Hidden")
    trending = BooleanField(
        default=False, help_text="0=default, 1=Trending")
    create_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Cart(Model):
    user = ForeignKey(User, on_delete=CASCADE)
    product = ForeignKey(Produk, on_delete=CASCADE)
    product_qty = IntegerField(null=False, blank=False)
    create_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Cart"


class Wishlist(Model):
    user = ForeignKey(User, on_delete=CASCADE)
    product = ForeignKey(Produk, on_delete=CASCADE)
    create_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Cart"


class Order(Model):
    user = ForeignKey(User, on_delete=CASCADE)
    fname = CharField(max_length=150, null=False)
    lname = CharField(max_length=150, null=False)
    email = CharField(max_length=150, null=False)
    phone = CharField(max_length=150, null=False)
    address = TextField(null=False)
    city = CharField(max_length=150, null=False)
    state = CharField(max_length=150, null=False)
    country = CharField(max_length=150, null=False)
    pincode = CharField(max_length=150, null=False)
    total_price = FloatField(null=False)
    payment_mode = CharField(max_length=150, null=False)
    payment_id = CharField(max_length=250, null=True)
    orderstatuses = (
        ('Pending', 'Pending'),
        ('Shipped', 'Shipped'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    )
    status = CharField(
        max_length=150, choices=orderstatuses, default='Pending')
    message = TextField(null=True)
    tracking_no = CharField(max_length=150, null=True)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def __str__(self):
        return '{} - {}'.format(self.id, self.tracking_no)


class OrderItem(Model):
    order = ForeignKey(Order, on_delete=CASCADE)
    product = ForeignKey(Produk, on_delete=CASCADE)
    price = FloatField(null=False)
    quantity = IntegerField(null=False)

    def __str__(self):
        return '{} {}'.format(self.order.id, self.order.tracking_no)


class Profile(Model):
    user = OneToOneField(User, on_delete=CASCADE)
    name = CharField(max_length=255, null=True, blank=True)
    phone = CharField(max_length=50, null=False)
    tgl_lahir = DateField(null=True, blank=True)
    address = TextField(null=False)
    city = CharField(max_length=150, null=False)
    state = CharField(max_length=150, null=False)
    country = CharField(max_length=150, null=False)
    pincode = CharField(max_length=150, null=False)
    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Pelanggan(Model):
    user = ForeignKey(User, on_delete=CASCADE)
    profile = ForeignKey(Profile, null=True, blank=True, on_delete=CASCADE)

    def __str__(self):
        return f"{self.user.username}'s Pelanggan"
