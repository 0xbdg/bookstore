from django.shortcuts import render
from django.http import JsonResponse
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
    return render(request, "pages/login.html", context={})

def signup(request):
    return render(request, "pages/signup.html", context={})

def settings(request):
    return render(request, "pages/profile_settings.html", context={})

def product_detail(request, id):
    buku = Buku.objects.get(id=id)
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

def transaction(request):
    return render(request, "pages/transaction.html")

@csrf_exempt
def status(request):
    try:
        if request.method == "POST":
            data = json.loads(request.body)
            fraud_status = data["fraud_status"]
            transaction_status = core_api.transactions.status(data["transaction_id"])

            if transaction_status == 'capture':
                if fraud_status == 'challenge':
                    Pemesanan(fraud_status="challenge").save()
                elif fraud_status == 'accept':
                    Pemesanan(fraud_status="accept").save()
            elif transaction_status == 'settlement':
                Pemesanan(transaction_status="settlement").save()
            elif transaction_status == 'cancel' or transaction_status == 'deny' or transaction_status == 'expire':
                Pemesanan(transaction_status="failure").save()
            elif transaction_status == 'pending':
                Pemesanan(transaction_status="pending").save()
            elif transaction_status == 'refund':
                Pemesanan(fraud_status="refund").save()

            print(data)

            return JsonResponse({"data":data})
    except:
        pass