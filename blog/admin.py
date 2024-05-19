from django.contrib import admin

# Register your models here.

from .models import Service, Tour, Parvoz, Yunalish

admin.site.register([Tour, Service, Parvoz, Yunalish])