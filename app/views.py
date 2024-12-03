from django.shortcuts import render

from .models import *
# Create your views here.

def index(request):
    if (request.method == "POST"):
        search = request.POST.get("pencarian")
        filter_buku = Buku.objects.filter(judul_buku__contains=search)
        return render(request, "pages/index.html", context={"produk":filter_buku})
    
    elif (request.method == "GET"):
        buku = Buku.objects.all()[::-1]
        return render(request, "pages/index.html", context={"produk":buku})
    
def signin(request):
    return render(request, "pages/login.html", context={})

def settings(request):
    return render(request, "pages/profile_settings.html", context={})

def product_detail(request, id):
    buku = Buku.objects.get(id=id)
    return render(request, "pages/product_detail.html", context={"produk":buku})

