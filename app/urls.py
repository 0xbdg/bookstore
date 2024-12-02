from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('product/<int:id>/', product_detail, name="detail")
]
