from django.db import models

from api.models.product import Product
from api.models.vending_machine import VendingMachine


class Stock(models.Model):
    id = models.AutoField(primary_key=True)
    vending_machine = models.ForeignKey(VendingMachine, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['vending_machine', 'product'], name='vending_machine_product')
        ]
