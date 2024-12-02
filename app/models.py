from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from djmoney.models.fields import MoneyField
# Create your models here.

class Buku(models.Model):
    sampul_buku = models.ImageField(upload_to="sampul/")
    judul_buku = models.CharField(max_length=255, null=False, blank=False)
    penulis_buku = models.CharField(max_length=255)
    deskripsi_buku = models.TextField(null=False, blank=False)
    jumlah_buku = models.IntegerField(null=False, blank=False)
    harga_buku = MoneyField(max_digits=100, decimal_places=2, default_currency='IDR')
    nomor_whatsapp = PhoneNumberField(region="ID")

    def __str__(self):
        return self.judul_buku

    class Meta:
        verbose_name = "Buku"
        verbose_name_plural = "Produk"

class Pemesanan(models.Model):
    pembeli = models.ForeignKey(User,on_delete=models.CASCADE)

