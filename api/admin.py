from django.contrib import admin
from .models import *


# Register your models here.
class BuyerAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'first_name']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


admin.site.register(Seller)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product, ProductAdmin)
admin.site.register(Buyer, BuyerAdmin)
admin.site.register(OrderProduct)
admin.site.register(WishList)
