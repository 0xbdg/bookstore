from django.shortcuts import render

from .models import *
from .midtrans import midtrans_client_key,snap

import datetime
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
    transaction_token = snap.create_transaction_token({
        "transaction_details": {
            "order_id": 878787,
            "gross_amount": 500000,
        }, "credit_card":{
            "secure" : True
        },
        "customer_details": {
            "first_name": "John A",
            "last_name": "Doe A",
            "email": "johndoe@email.com",
            "phone": "+62812345678",
            "address":""
        },
        "product_details": {
            "product_id":"",
            "product_name":"",
            "quantity": buku.jumlah_buku,
            "price": 500000
        }
    })
    return render(request, "pages/product_detail.html", context={"produk":buku, "client_key":midtrans_client_key, "token":transaction_token})

