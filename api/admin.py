from django.contrib import admin

from api.models.product import Product
from api.models.stock import Stock
from api.models.vending_machine import VendingMachine

admin.site.register(VendingMachine)
admin.site.register(Product)
admin.site.register(Stock)
