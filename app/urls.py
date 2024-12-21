from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('about/', about, name="tentang"),
    path('accounts/login/', signin, name="login"),
    path('logout/', signout, name="logout"),
    path('accounts/register/', signup, name="signup"),
    path('settings/', settings, name="profile"),
    path('transaction/', transaction, name="transaction"),
    path('cart/', cart, name="cart"),
    path('product/<int:id>/', product_detail, name="detail"),
    path("transaksi/pembayaran/<uuid:product_id>", checkout, name="pembayaran")
]
