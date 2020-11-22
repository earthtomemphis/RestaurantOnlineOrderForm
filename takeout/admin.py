from django.contrib import admin
from .models import Order, Menu

# Register your models here.
admin.site.register(Menu)
admin.site.register(Order)