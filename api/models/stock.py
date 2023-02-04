from typing import List

from django.db import models
from django.db.models import AutoField, PositiveIntegerField, UniqueConstraint

from api.models.product import Product
from api.models.vending_machine import VendingMachine


class Stock(models.Model):
    id: AutoField = models.AutoField(primary_key=True)
    vending_machine: VendingMachine = models.ForeignKey(VendingMachine, on_delete=models.CASCADE)
    product: Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity: PositiveIntegerField = models.PositiveIntegerField()

    class Meta:
        constraints: List[UniqueConstraint] = [
            models.UniqueConstraint(fields=['vending_machine', 'product'], name='vending_machine_product')
        ]
