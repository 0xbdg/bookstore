from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('login/', signin, name="login"),
    path('settings/', settings, name="profile"),
    path('product/<int:id>/', product_detail, name="detail")
]
