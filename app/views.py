from django.shortcuts import render

from .models import *
# Create your views here.

def index(request):
    buku = Buku.objects.all()[::-1]
    return render(request, "pages/index.html", context={"produk":buku})

def product_detail(request, id):
    buku = Buku.objects.get(id=id)
    return render(request, "pages/product_detail.html", context={"produk":buku})

