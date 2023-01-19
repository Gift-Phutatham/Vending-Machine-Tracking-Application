from django.db import models

from api.models.product import Product
from api.models.vending_machine import VendingMachine


class Stock(models.Model):
    vending_machine = models.ForeignKey(VendingMachine, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
