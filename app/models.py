from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from djmoney.models.fields import MoneyField
from django.core.exceptions import ValidationError
import re, uuid
# Create your models here.

def validate_isbn(value):
    isbn13_regex = r'^\d{3}-\d{1,5}-\d{1,7}-\d{1,7}-\d{1}$'
    isbn10_regex = r'^\d{1,5}-\d{1,7}-\d{1,7}-\d{1}$'
    
    if not re.match(isbn13_regex, value) and not re.match(isbn10_regex, value):
        raise ValidationError(f"{value} is not a valid ISBN.")

class Buku(models.Model):
    sampul_buku = models.ImageField(upload_to="sampul/")
    judul_buku = models.CharField(max_length=255, null=False, blank=False)
    penulis_buku = models.CharField(max_length=255)
    deskripsi_buku = models.TextField(null=False, blank=False)
    harga_buku = models.IntegerField(null=False)
    kategori = models.CharField(max_length=255)
    isbn = models.CharField(max_length=17, unique=True, validators=[validate_isbn])
    publisher_buku = models.CharField(max_length=255,null=False, blank=False)
    tanggal_publikasi = models.DateField(null=False,blank=False)
    lembar_buku = models.IntegerField(null=False,blank=False)
    bahasa = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.judul_buku

    class Meta:
        verbose_name = "Buku"
        verbose_name_plural = "Produk"

class Transaksi(models.Model):
    token = models.CharField(max_length=255, null=False, blank=False)
    pembeli = models.ForeignKey(User,on_delete=models.CASCADE)
    order_id = models.CharField(max_length=10)
    produk = models.CharField(max_length=255, null=False, blank=False)
    transaction_status = models.CharField(max_length=255)

class Keranjang(models.Model):
    id = models.CharField(primary_key=True, max_length=255, default=uuid.uuid1())
    order_id = models.CharField(max_length=10, null=False, blank=False)
    pembeli = models.ForeignKey(User, on_delete=models.CASCADE)
    produk = models.CharField(max_length=255, null=False)
    harga=models.IntegerField(null=False)
