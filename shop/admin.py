from django.contrib import admin
from .models import Products, Cart, CartItem

admin.site.register(Products)
admin.site.register(Cart)
admin.site.register(CartItem)
