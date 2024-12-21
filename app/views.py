from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from .forms import *
from .models import *
from .midtrans import midtrans_client_key,snap, core_api

import datetime, random, string,json
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
    form = SignIn(data=request.POST)

    if form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect("profile")
    
    return render(request, "pages/login.html", context={"form":form})

def signup(request):
    form = SignUp(request.POST)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("login")
    return render(request, "pages/signup.html", context={"form":form})

@login_required
def settings(request):
    return render(request, "pages/profile_settings.html", context={})

def product_detail(request, id):
    buku = Buku.objects.get(id=id)
    if request.method == "POST":
        if "login_dulu" in request.POST:
            return redirect("login")
        user = User.objects.get(username=request.user.get_username())
        keranjang = Keranjang(pembeli=user, order_id="".join(random.choices(string.ascii_letters + string.digits, k=10)),produk=buku.judul_buku, jumlah=request.POST["quantity"])
        keranjang.save()
        return redirect("cart")

    transaction_token = snap.create_transaction_token({
        "transaction_details": {
            "order_id": ''.join(random.choices(string.ascii_letters + string.digits, k=10)),
            "gross_amount": 500000,
        }, "credit_card":{
            "secure" : True
        },
        "customer_details": {
            "first_name": "John A",
            "last_name": "Doe A",
            "email": "johndoe@email.com",
            "phone": "+62812345678",
        },
        "product_details": {
            "product_id":"",
            "product_name":"",
            "quantity": buku.jumlah_buku,
            "price": 500000
        }
    })
    return render(request, "pages/product_detail.html", context={"produk":buku, "client_key":midtrans_client_key, "token":transaction_token})

@login_required
def cart(request):
    keranjang = Keranjang.objects.all()

    if request.method=="POST":
        if "delete" in request.POST:
            product_id = request.POST["product_id"]
            hapus = Keranjang.objects.get(id=product_id)
            hapus.delete()  
        
        if "update" in request.POST:
            product_id = request.POST["product_id"]
            update = Keranjang.objects.get(id=product_id)
    return render(request, "pages/cart.html", context={"lists":keranjang})

@login_required
def transaction(request):
    return render(request, "pages/transaction.html")

@login_required
def signout(request):
    logout(request)
    return redirect("index")

def checkout(request):
    return render(request, "pages/pembayaran.html")