from django.contrib import admin

from .models import Buku

# Register your models here.

admin.site.site_title = "Book Store"
admin.site.index_title = "Admin Panel"
admin.site.site_header = "Book Store"

admin.site.register(Buku)
