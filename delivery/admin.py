from django.contrib import admin
from .models import *

# Register your models here.

# user:admin
# pass:1234
class PackAdmin(admin.ModelAdmin):
    list_display = ['trackingNumber', 'sku']

admin.site.register(Pack, PackAdmin)
